from classes import task
from functions import add, delete, update_assignments, find

task_list = [
    "Math homework",
    "Science project",
    "English essay",
    "History research",
    "Programming exercises",
    "Art project",
    "Reading assignment",
]


while True:
    option=input("""
1. Add new task
2. edit taks
3. search task
4. delete task
""")
    if option=="1":
        name=input("task name: ")
        starting_date=input("task starting_date: ")
        finish_date=input("finish_date: ")
        man_responsible=input("man_responsible is: ")
        task_discretion=input("task_discretion is" :)
        category=input("category: ")
        add(task(name=name, starting_date=starting_date, finish_date=finish_date, man_responsible=man_responsible, task_discretion=task_discretion, category=category))

    if option=="2":
        name=input("name: ")
        new_name=input("new name: ")
        starting_date=input("new starting_date: ")
        finish_date=input("new finish_date: ")
        man_responsible=input("new man_responsible: ")
        task_discretion=input("new task_discretion: ")
        category=input("new category: ")
        update_assignments(name=name, new_name=new_name, starting_date=starting_date, finish_date=finish_date, man_responsible=man_responsible, task_discretion=task_discretion, category=category)

    if option=="3":



     if option=="4":
        name=input("name: ")
        delete(name=name)
           