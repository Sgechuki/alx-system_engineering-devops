#!/usr/bin/python3
"""script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress"""
import csv
import requests
import sys


user_no = int(sys.argv[1])
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
        user_id = task.get("userId")
        title = task.get("title")
        comp = task.get("completed")
        user_tasks.append([user_id, username, title, comp])
with open("{}.csv".format(user_no), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(user_tasks)
