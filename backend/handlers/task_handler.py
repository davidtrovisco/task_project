from backend.services.task_service import add, get_tasks, get_task, update_task, delete_task

def get_task_service():
    return {
        "add": add,
        "get_tasks": get_tasks,
        "get_task": get_task,
        "update_task": update_task,
        "delete_task": delete_task
    }
def get_task_service_keys():
    return ["add", "get_tasks", "get_task", "update_task", "delete_task"]

def list_task_service():
    return get_task_service()

def list_task_service_keys():
    return get_task_service_keys()
def list_task_service_and_keys():
    return {
        "service": list_task_service(),
        "keys": list_task_service_keys()
    }
