def display_menu():
    print("Menu:\n")
    return "1. Include\n2. List\n3. Done\n4. Remove\n5. Exit\n"
    

def include_task(tasks):
    content = input("Enter a task: ").strip().lower()
    if not content:
        print("Entered empty input. Task not added.")
    else:
        tasks.append([content, False])
        print("Task added.")
    return tasks


def all_tasks(tasks):
    
    return tasks
    
    
def comp_tasks(tasks, content):
    done = input("Enter task done or not (yes/no): ").strip().lower()
    for task in tasks:
        if task[0].strip().lower() == content:
            if done in ("yes", "y"):
                task[1] = True
                print(f"{content} is done.")
            elif done in ("no", "n"):
                task[1] = False
                print(f"{content} is not done.")
            else:
                print("Invalid input. Type (yes/no).")
            return tasks
    print(f"{content} not found.")
    return tasks
    
def del_task(tasks, content):
    delete = input("Enter what to delete:")
    if not delete:
        print("Nothing is deleted.")
    else:    
        tasks.pop(content)
    
    return tasks