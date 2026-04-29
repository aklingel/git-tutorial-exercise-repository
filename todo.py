class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def __str__(self):
        status = "x" if self.done else " "
        return f"[{status}] {self.title}"


def add_task(tasks, title):
    tasks.append(Task(title))


def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def remove_task(tasks, index):
    tasks.pop(index - 1)


if __name__ == "__main__":
    tasks = []
    add_task(tasks, "Buy groceries")
    add_task(tasks, "Write unit tests")
    list_tasks(tasks)
    remove_task(tasks, 1)
    list_tasks(tasks)
