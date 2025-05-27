import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")


# Function to add a task to the file
def add_task(task, filename="tasks.txt"):
    with open(filename, "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' has been added.")


# Function to view all tasks
def view_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
        if tasks:
            print("\nTo-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your to-do list is empty!")
    else:
        print("No tasks found.")


# Function to remove a task
def remove_task(task_number, filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open(filename, "w") as file:
                file.writelines(tasks)
            print(f"Task '{removed_task.strip()}' has been removed.")
        else:
            print("Invalid task number!")
    else:
        print("No tasks found.")


# Function to handle the user input and run the program
def main():
    while True:
        display_menu()

        choice = input("Choose an option (1-4): ")

        if choice == '1':  # Add task
            task = input("Enter the task you want to add: ")
            add_task(task)

        elif choice == '2':  # View tasks
            view_tasks()

        elif choice == '3':  # Remove task
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':  # Exit
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
