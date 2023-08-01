from files import load_items, save_items
from classes import task
from app import task_list, name 

def add(task:task):
    items=load_items()
    items.append(task)
    save_items(items=items)


def delete(task="task"):
    items=load_items() 
    for task in task_list.copy():
        if task.name==name:
            task.remove(task)
    save_items(task)

def update_assignments(task="task"):
    items=load_items() 
    for task in task_list:
        if str(task.name)==name:
            task.update_assignments=name
            print("task is updated")
    save_items(items=task)
       

def find():
    task=input("task name: ")
    for task in task_list:
        if str(task.name)==name:
            print(task)    
