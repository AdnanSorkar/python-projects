def display_menu():
    print("Menu:\n")
    return "1. Include\n2. List\n3. Done\n4. Remove\n5. Exit\n"
    

def include_task(tasks):
    content = input("Enter a task: ").strip()
    if not content:
        print("Empty input. Task not added.")
    else:
        tasks.append([content, False])
        print("Task added.")
    return tasks


def all_tasks(tasks):
    return 
    
    
def comp_tasks(tasks):
    done = input("Enter task done or not:")
    
    return 
    
    
def del_tasks(tasks):
    return 