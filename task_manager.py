"""
    Name: task_manager.py
    Author: Triumph Ogbonnia
    Created: 4/18/24
    Purpose: Store user tasks
"""

import json
import random
from rich.panel import Panel
from rich.console import Console

console = Console()

# Define global variables
users_file = "users.json"
tasks_file = "tasks.json"

# Function to load user data from file
def load_users():
    try:
        with open(users_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user data to file
def save_users(users):
    with open(users_file, "w") as file:
        json.dump(users, file)

# Function to load task data from file
def load_tasks():
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save task data to file
def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        json.dump(tasks, file)

# Function for user registration
def register_user(username, password):
    users = load_users()
    if username in users:
        print("\nUsername already exists. Please choose another one.")
        return
    users[username] = {"password": password, "tasks": []}
    save_users(users)
    print("\nUser registered successfully.")

# Function for user login
def login_user(username, password):
    users = load_users()
    if username not in users or users[username]["password"] != password:
        print("Invalid username or password.")
        return None
    print("Login successful.")
    return username

# Function to add a new task
def add_task(username, task_name, due_date):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "name": task_name, "due_date": due_date})
    save_tasks(tasks)
    users = load_users()
    users[username]["tasks"].append(task_id)
    save_users(users)
    print("Task added successfully.")

# Function to display user's tasks
def display_tasks(username):
    tasks = load_tasks()
    users = load_users()
    user_tasks = users[username]["tasks"]
    print("\nYour Tasks:")
    for task_id in user_tasks:
        task = next((task for task in tasks if task["id"] == task_id), None)
        if task:
            print(f"Task ID: {task['id']}\nName: {task['name']}\nDue Date: {task['due_date']}\n------------------------")
        else:
            print(f"Task with ID {task_id} not found.")
    if not user_tasks:
        print("You have no tasks.")

# Function to generate random tasks for demonstration
def generate_random_tasks():
    tasks = []
    for i in range(10):
        task_name = f"Task {i+1}"
        due_date = f"2024-04-{random.randint(1, 30)}"
        tasks.append({"id": i+1, "name": task_name, "due_date": due_date})
    return tasks

# Main function
def main():
    console.print(
        Panel.fit(
            "   ****    Task Manager    ****   ",
            subtitle="By Triumph Ogbonnia",
            style="bold blue"
        )
    )
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            user = login_user(username, password)
            if user:
                while True:
                    print("\n1. Add Task\n2. View Tasks\n3. Logout")
                    user_choice = input("\nEnter your choice: ")
                    if user_choice == "1":
                        task_name = input("\nEnter task name: ")
                        due_date = input("Enter due date (YYYY-MM-DD): ")
                        add_task(username, task_name, due_date)
                    elif user_choice == "2":
                        display_tasks(username)
                    elif user_choice == "3":
                        print("\nLogged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()