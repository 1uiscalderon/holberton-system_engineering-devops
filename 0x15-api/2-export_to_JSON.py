#!/usr/bin/python3
"""Using the REST API from https://jsonplaceholder.typicode.com/, for a given
employee ID, returns information about his/her TODO list progress, the export
it to JASON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    f_name = argv[1] + ".json"
    info = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    user = requests.get(info).json()
    tasksuser = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    tasks = requests.get(tasksuser).json()
    dict_ = []
    for task in tasks:
        dict_.append({"task": task.get("title"),
                     "completed": task.get("completed"),
                      "username": user.get("name")})
    with open(f_name, 'w', newline='') as f:
        d = {}
        d[argv[1]] = dict_
        f.write(json.dumps(d))
