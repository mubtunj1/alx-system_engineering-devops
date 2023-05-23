#!/usr/bin/python3
""" Accessing todo list"""
import requests
import sys
import json

if __name__ == "__main__":
    employee_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    Url = baseUrl + "/" + employee_id
    response = requests.get(Url)
    Username = response.json().get('username')

    to_do = Url + '/todos'
    response = requests.get(to_do)
    tasks = response.json()

    dictionary = {employee_id: []}
    for task in tasks:
        dictionary[employee_id].append({"task": task.get('title'),
                                        "completed": task.get('completed'),
                                       "username": Username})

    with open('{}.json'.format(employee_id), 'w') as filename:
        json.dump(dictionary, filename)


