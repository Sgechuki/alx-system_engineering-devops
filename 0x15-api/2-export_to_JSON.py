#!/usr/bin/python3
"""script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress"""
import json
import requests
import sys


def to_json(user_no):
    api_url_1 = "https://jsonplaceholder.typicode.com/todos/"
    tasks_res = requests.get(api_url_1)
    tasks = tasks_res.json()
    api_url_2 = "https://jsonplaceholder.typicode.com/users"
    users_res = requests.get(api_url_2)
    users = users_res.json()
    username = str()
    for user in users:
        if user.get("id") == user_no:
            username = user.get("username")
    user_tasks = []
    for task in tasks:
        if task.get("userId") == user_no:
            title = task.get("title")
            comp = task.get("completed")
            user_tasks.append({"task": title,
                              "completed": comp, "username": username})
    all_usr = dict()
    all_usr[str(user_no)] = user_tasks
    with open("{}.json".format(user_no), "w") as f:
        json.dump(all_usr, f)


if __name__ == "__main__":
    to_json(int(sys.argv[1]))
