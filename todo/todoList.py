import json
from datetime import datetime

#global list to store tasks
tasks = []

#file name for saving and loading tasks
filename = "todo.json"

def add_task(description, deadline, priority):
    task = {
        'description': description,
        'deadline': deadline,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    save_tasks()

def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks()
    else:
        print("Invalid task number.")

def mark_task_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks()
    else:
        print("Invalid task number.")

def save_tasks():
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")

def display_tasks():
    for i, task in enumerate(tasks):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{i + 1}. {task['description']} - {task['deadline']} - Priority: {task['priority']} - {status}")

def main():
    load_tasks()
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. Display Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            priority = int(input("Enter task priority (1-5): "))
            add_task(description, deadline, priority)
        elif choice == '2':
            display_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            remove_task(index)
        elif choice == '3':
            display_tasks()
            index = int(input("Enter task number to mark as complete: ")) - 1
            mark_task_complete(index)
        elif choice == '4':
            display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
