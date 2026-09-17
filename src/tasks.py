import uuid
from src.storage import load_tasks, save_tasks
from src.models import Task

def get_user_tasks(username):
    tasks = load_tasks()
    return tasks.get(username, [])

def add_task(username, title, description, priority):
    tasks = load_tasks()
    if username not in tasks:
        tasks[username] = []
    
    task_id = str(uuid.uuid4())[:8]
    new_task = Task(task_id, title, description, priority).to_dict()
    tasks[username].append(new_task)
    save_tasks(tasks)
    return True, "Task added successfully."

def delete_task(username, task_id):
    tasks = load_tasks()
    user_tasks = tasks.get(username, [])
    original_length = len(user_tasks)
    
    tasks[username] = [t for t in user_tasks if t['task_id'] != task_id]
    
    if len(tasks[username]) < original_length:
        save_tasks(tasks)
        return True, "Task deleted."
    return False, "Task not found."

def update_task_status(username, task_id, new_status):
    tasks = load_tasks()
    user_tasks = tasks.get(username, [])
    for t in user_tasks:
        if t['task_id'] == task_id:
            t['status'] = new_status
            save_tasks(tasks)
            return True, "Task status updated."
    return False, "Task not found."
