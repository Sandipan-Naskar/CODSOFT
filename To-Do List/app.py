from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'done': False})
    return redirect('/')

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    tasks[task_id]['done'] = not tasks[task_id]['done']
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
