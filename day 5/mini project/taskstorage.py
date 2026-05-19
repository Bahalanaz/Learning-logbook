def taskstorage():
    internal_storage = []
    logs = []
    task_id_counter = 1

    current_user = {"logged_in": True}

    def add_log(msg):
        logs.append(msg)

    def login_required(func):
        def wrapper(*args, **kwargs):
            if not current_user["logged_in"]:
                print("Access denied: user not logged in")
                return
            return func(*args, **kwargs)
        return wrapper

    def log_function(func):
        def wrapper(*args, **kwargs):
            print(f"[LOG] {func.__name__} started")
            result = func(*args, **kwargs)
            print(f"[LOG] {func.__name__} finished")
            return result
        return wrapper

    def validate_task_id(func):
        def wrapper(task_id, *args, **kwargs):
            if not isinstance(task_id, int) or task_id <= 0:
                print("Invalid task ID")
                return
            return func(task_id, *args, **kwargs)
        return wrapper

    @login_required
    @log_function
    def add_task(name):
        nonlocal task_id_counter

        task = {
            "id": task_id_counter,
            "name": name,
            "status": "pending"
        }

        internal_storage.append(task)
        task_id_counter += 1

        add_log("task added")

    @login_required
    @log_function
    def view_tasks():
        add_log("task viewed")
        return internal_storage

    @login_required
    @log_function
    @validate_task_id
    def complete_task(task_id):
        for task in internal_storage:
            if task["id"] == task_id:
                task["status"] = "done"
                add_log("task completed")
                return task

        print("no task found")

    @login_required
    @log_function
    @validate_task_id
    def delete_task(task_id):
        for task in internal_storage:
            if task["id"] == task_id:
                internal_storage.remove(task)
                add_log("task removed")
                return task

        print("this does not exist")

    @login_required
    def view_logs():
        return logs

    return {
        "add_task": add_task,
        "view_tasks": view_tasks,
        "complete_task": complete_task,
        "delete_task": delete_task,
        "view_logs": view_logs
    }