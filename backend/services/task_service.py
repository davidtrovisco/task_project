task = []

def add(new_task):
    task.append(new_task)
    return new_task

def get_tasks():
    return task

def get_task(index):
    if 0 <= index < len(task):
        return task[index]
    return None

def update_task(index, updated_task):
    if 0 <= index < len(task):
        task[index] = updated_task
        return updated_task
    return None

def delete_task(index):
    if 0 <= index < len(task):
        return task.pop(index)
    return None
