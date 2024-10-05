from tinydb import TinyDB, Query

db = TinyDB('db.json')

def get_todos(todo_id=None):
    if todo_id:
        return db.get(doc_id=todo_id)
    return db.all()

def add_todo(todo_text):
    db.insert({'todo': todo_text})

def delete_todo(todo_id):
    db.remove(doc_ids=[todo_id])

def update_todo(todo_id, new_text):
    db.update({'todo': new_text}, doc_ids=[todo_id])
