# cli.py
import asyncio
import sys
from task_manager import add_task, view_tasks, complete_task, remove_task  

async def menu():
    print("Welcome to the To-Do List Manager!")
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Remove Task\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            await add_task_cli()
        elif choice == '2':
            await view_tasks_cli()
        elif choice == '3':
            await complete_task_cli()
        elif choice == '4':
            await remove_task_cli()
        elif choice == '5':
            print("Exiting...")
            sys.exit()

async def add_task_cli():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    await add_task(title, description, due_date)
    print("Task added successfully!")

async def view_tasks_cli():
    await view_tasks()

async def complete_task_cli():
    index = int(input("Enter the index of the task to mark as completed: "))
    await complete_task(index)
    print("Task marked as completed!")

async def remove_task_cli():
    index = int(input("Enter the index of the task to remove: "))
    await remove_task(index)
    print("Task removed successfully!")
    
