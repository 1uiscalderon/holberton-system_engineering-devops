#!/usr/bin/python3
"""Using the REST API from https://jsonplaceholder.typicode.com/, for a given
employee ID, returns information about his/her TODO list progress, the export
it to csv format"""
import requests
from sys import argv
import csv


if __name__ == "__main__":
    f_name = argv[1] + ".csv"
    info = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    user = requests.get(info).json()
    tasksuser = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    tasks = requests.get(tasksuser).json()
    with open(f_name, 'w', newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            w.writerow([user['id'], user['username'],
                        task['completed'], task['title']])
