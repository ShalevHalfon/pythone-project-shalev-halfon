from classes import task
from functions import add, delete, update_assignments, find
import random
from files import load_items


def find():
    task=input("task name: ")
    for task in tasks:
        if str(task.name)==neme:
            print(task)

def creat_task():
               