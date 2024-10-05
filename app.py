from flask import Flask, render_template, request, redirect, url_for
from models import get_todos, add_todo, delete_todo, update_todo

app = Flask(__name__)

# Display To-Do List
@app.route('/')
def index():
    todos = get_todos()
    return render_template('index.html', todos=todos)

# Add new task
@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    add_todo(todo)
    return redirect(url_for('index'))

# Delete task
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for('index'))

# Edit task - show edit form
@app.route('/edit/<int:todo_id>')
def edit(todo_id):
    todo = get_todos(todo_id)
    return render_template('edit.html', todo=todo)

# Update task after editing
@app.route('/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    updated_text = request.form.get('todo')
    update_todo(todo_id, updated_text)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
