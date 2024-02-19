#!/usr/bin/python3
"""script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress"""
import json
import requests
import sys


def tasks(user_no, username):
    api_url_1 = "https://jsonplaceholder.typicode.com/todos/"
    tasks_res = requests.get(api_url_1)
    tasks = tasks_res.json()
    user_tasks = []
    for task in tasks:
        if task.get("userId") == user_no:
            title = task.get("title")
            comp = task.get("completed")
            user_tasks.append({"username": username, "task": title,
                              "completed": comp})
    return user_tasks


def all_todos():
    api_url_2 = "https://jsonplaceholder.typicode.com/users"
    users_res = requests.get(api_url_2)
    users = users_res.json()
    all_usrs_tasks = {}
    for user in users:
        user_no = user.get("id")
        username = user.get("username")
        all_usrs_tasks[user_no] = tasks(user_no, username)
    with open("todo_all_employees.json".format(user_no), "w") as f:
        json.dump(all_usrs_tasks, f)


if __name__ == "__main__":
    all_todos()
