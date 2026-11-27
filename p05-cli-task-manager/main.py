from tasks import display_menu, include_task, all_tasks, comp_tasks, del_task

tasks = []

while True:
    menu = display_menu()
    if menu is not None:
        print(menu)

    menuOpt = input("Select a option: ").strip()

    if not menuOpt:
        print("Empty input. Try again.")
        continue
    try:
        menuOpt = int(menuOpt)
    except ValueError:
        print("Give a number. Try again.")
        continue

    if menuOpt == 1:
        content = input("Enter a task: ").strip().lower()
        tasks = include_task(tasks, content)
    elif menuOpt == 2:
        tasks = all_tasks(tasks)
    elif menuOpt == 3:
        content = input("Enter task name: ").strip().lower()
        done = input("Enter task done or not (yes/no): ").strip().lower()
        tasks = comp_tasks(tasks, content, done)
    elif menuOpt == 4:
        delete = input("Enter the task no. to delete: ").strip()
        tasks = del_task(tasks, delete)
    elif menuOpt == 5:
        break
    else:
        print("Invalid option. Choose a number from 1 to 5.")