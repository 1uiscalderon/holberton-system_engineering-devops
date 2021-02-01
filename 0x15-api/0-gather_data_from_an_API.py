#!/usr/bin/python3
"""Using the REST API from https://jsonplaceholder.typicode.com/, for a given
employee ID, returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    info = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    name = requests.get(info).json().get("name")
    tasksuser = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    tasks = requests.get(tasksuser).json()
    list_comp = []
    for completed in tasks:
        if completed.get("completed"):
            list_comp.append((completed.get("title")))
    print("Employee {} is done with tasks({}/{}):".format(name, len(list_comp),
                                                          len(tasks)))
    for i in list_comp:
        print("\t {}".format(i))
