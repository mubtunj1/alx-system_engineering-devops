#!/usr/bin/python3
""" Accessing todo list"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    Url = baseUrl + "/" + employee_id
    response = requests.get(Url)
    employee_name = response.json().get('name')

    to_do = Url + '/' + 'todos'
    response = requests.get(to_do)
    tasks = response.json()

    done = 0
    done_task = []

    for task in tasks:
        if task.get('completed'):
            done_task.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))

    for task in done_task:
        print("\t {}".format(task.get('title')))
