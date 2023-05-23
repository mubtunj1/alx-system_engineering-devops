#!/usr/bin/python3
""" Accessing todo list"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    Url = baseUrl + "/" + employee_id
    response = requests.get(Url)
    Username = response.json().get('username')

    to_do = Url + '/todos'
    response = requests.get(to_do)
    tasks = response.json()

    with open("{}.csv".format(employee_id), 'w') as file:
        for task in tasks:
            print('"{}","{}","{}","{}"\n'
                  .format(employee_id, Username, task.get('completed'),
                          task.get('title')))
