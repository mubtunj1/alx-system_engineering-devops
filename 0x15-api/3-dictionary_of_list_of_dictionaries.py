#!/usr/bin/python3
""" Accessing todo list"""
import json
import requests
import sys

if __name__ == "__main__":

    baseUrl = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(baseUrl)
    Users = response.json()

    dictionary = {}

    for user in Users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'\
              .format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
