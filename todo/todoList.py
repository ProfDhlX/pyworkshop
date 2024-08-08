# Global list to store tasks
task_list = []

# File name for saving and loading tasks
task_file = "todo.txt"

def add_task(task_description, task_deadline, task_priority):
    new_task = {
        'description': task_description,
        'deadline': task_deadline,
        'priority': task_priority,
        'completed': False
    }
    task_list.append(new_task)
    save_tasks()

def remove_task(task_index):
    if 0 <= task_index < len(task_list):
        del task_list[task_index]
        save_tasks()
    else:
        print("Invalid task number.")

def mark_task_complete(task_index):
    if 0 <= task_index < len(task_list):
        task_list[task_index]['completed'] = True
        save_tasks()
    else:
        print("Invalid task number.")

def save_tasks():
    with open(task_file, 'w') as file:
        for task in task_list:
            task_data = f"{task['description']},{task['deadline']},{task['priority']},{task['completed']}\n"
            file.write(task_data)

def load_tasks():
    global task_list
    try:
        with open(task_file, 'r') as file:
            for line in file:
                task_description, task_deadline, task_priority, task_completed = line.strip().split(',')
                loaded_task = {
                    'description': task_description,
                    'deadline': task_deadline,
                    'priority': int(task_priority),
                    'completed': task_completed == 'True'
                }
                task_list.append(loaded_task)
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")

def display_tasks():
    for index, task in enumerate(task_list):
        task_status = 'Done' if task['completed'] else 'Pending'
        print(f"{index + 1}. {task['description']} - {task['deadline']} - Priority: {task['priority']} - {task_status}")

def main():
    load_tasks()
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. Display Tasks")
        print("5. Exit")
        
        user_choice = input("Choose an option: ")

        if user_choice == '1':
            task_description = input("Enter task description: ")
            task_deadline = input("Enter task deadline (YYYY-MM-DD): ")
            task_priority = int(input("Enter task priority (1-5): "))
            add_task(task_description, task_deadline, task_priority)
        elif user_choice == '2':
            display_tasks()
            task_index = int(input("Enter task number to remove: ")) - 1
            remove_task(task_index)
        elif user_choice == '3':
            display_tasks()
            task_index = int(input("Enter task number to mark as complete: ")) - 1
            mark_task_complete(task_index)
        elif user_choice == '4':
            display_tasks()
        elif user_choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
