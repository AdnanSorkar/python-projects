from tasks import display_menu, include_task, all_tasks, comp_tasks, del_tasks

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
        include_task(tasks)
    elif menuOpt == 2:
        all_tasks(tasks)
    elif menuOpt == 3:
        comp_tasks(tasks)
    elif menuOpt == 4:
        del_tasks(tasks)
    elif menuOpt == 5:
        break
    else:
        print("Invalid option. Choose a number from 1 to 5.")