def display_menu():
    print("Menu:\n")
    return "1. Include\n2. List\n3. Done\n4. Remove\n5. Exit\n"
    

def include_task(tasks):
    content = input("Enter a task: ").strip()
    if not content:
        print("Entered empty input. Task not added.")
    else:
        tasks.append([content, False])
        print("Task added.")
    return tasks


def all_tasks(tasks):
    
    return tasks
    
    
def comp_tasks(tasks, content):
    done = input("Enter task done or not:")
    if not done:
        tasks.append([content, False])
    else:
        tasks.append([content, True])
        print("Task added.")
    return tasks
    
    
def del_tasks(tasks, content):
    delete = input("Enter what to delete:")
    if not delete:
        print("Nothing is deleted.")
    else:    
        tasks.pop(content)
    
    return tasks