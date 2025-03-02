tasks = []  # Global list to store tasks

def addTask():
    task = input("Please enter a Task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

def deleteTask():
    listTasks()
    if not tasks:
        return  # No tasks to delete
    
    try:
        taskToDelete = int(input("Enter the task number to delete: "))
        if 0 <= taskToDelete < len(tasks): 
            removed_task = tasks.pop(taskToDelete)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print(f"Task #{taskToDelete} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

if __name__ == "__main__":
    print("Welcome to the To-Do List App:")
    while True: 
        print("\nPlease select one of the following options:")
        print("-------------------------------------")
        print("1. Add New Task")
        print("2. Delete a Task")
        print("3. List All Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            addTask()
        elif choice == '2':
            deleteTask()
        elif choice == '3':
            listTasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
