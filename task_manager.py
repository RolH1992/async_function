# task_management.py
import asyncio
from data_model import Task  

tasks = []

async def add_task(title, description, due_date):
    tasks.append(Task(title, description, due_date))

async def view_tasks():
    for task in tasks:
        print(task)

async def complete_task(index):
    tasks[index].completed = True

async def remove_task(index):
    if index < len(tasks):
        del tasks[index]
    else:
        print("Invalid index. Task not found.")
