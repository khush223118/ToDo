import os
import json
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

# Function to remove a task
def remove_task(tasks):
    print_tasks(tasks)
    index = int(input("Enter index of task to remove: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task removed successfully!")
    else:
        print("Invalid index.")

# Function to mark a task as completed
def mark_completed(tasks):
    print_tasks(tasks)
    index = int(input("Enter index of task to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid index.")

# Function to display tasks
def print_tasks(tasks):
    print("\nTask List:")
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['name']} (Priority: {task['priority']}, Due: {task['due_date']})")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
