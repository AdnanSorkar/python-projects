def display_menu():
    print("Menu:\n")
    return "1. Include\n2. List\n3. Done\n4. Remove\n5. Exit\n"


def include_task(tasks, content):
    if not content:
        print("Entered empty input. Task not added.")
    else:
        tasks.append([content, False])
        print(f"Task ({len(tasks)}) '{content}' is added.")

    return tasks


def all_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return tasks

    for num, task in enumerate(tasks, start=1):
        title = task[0]
        comp = task[1]
        status = "Done" if comp else "Not done"
        print(f"({num}) '{title}' is {status}")

    return tasks


def comp_tasks(tasks, content, done):
    for task in tasks:
        if task[0].strip().lower() == content:
            if done in ("yes", "y"):
                task[1] = True
                print(f"'{content}' is done.")
            elif done in ("no", "n"):
                task[1] = False
                print(f"'{content}' is not done.")
            else:
                print("Invalid input. Type (yes/no).")

            return tasks

    print(f"'{content}' not found.")
    return tasks


def del_task(tasks, delete):
    if not delete:
        print("Nothing is deleted.")
        return tasks

    try:
        dltkNum = int(delete)
    except ValueError:
        print("Please enter a valid number.")
        return tasks

    idx = dltkNum - 1
    if idx < 0 or idx >= len(tasks):
        print("Task number is out of range.")
        return tasks

    taskDlt = tasks.pop(idx)
    print(f"Task ({dltkNum}) '{taskDlt[0]}' is deleted.")
    return tasks