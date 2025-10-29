from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)
tasks = []
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'id': len(tasks) + 1, 'task': task})
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit_task(id):
    task=next((t for t in tasks if t['id']==id),None)
    return render_template('edit.html', task=task)

@app.route('/update/<int:id>',methods=['POST'])
def update_task(id):
    new_task=request.form.get('task')
    for t in tasks:
        if t['id']==id:
            t['task']=new_task
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)