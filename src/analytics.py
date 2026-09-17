from src.tasks import get_user_tasks

def generate_report(username):
    tasks = get_user_tasks(username)
    total = len(tasks)
    if total == 0:
        return {"total": 0, "completed": 0, "pending": 0, "completion_rate": "0%"}
    
    completed = sum(1 for t in tasks if t['status'] == 'Completed')
    pending = total - completed
    rate = (completed / total) * 100
    
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_rate": f"{rate:.1f}%"
    }
