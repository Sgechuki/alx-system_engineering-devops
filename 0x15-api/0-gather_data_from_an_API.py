#!/usr/bin/python3
"""script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress"""
import requests
import sys

user_no = int(sys.argv[1])
api_url_1 = "https://jsonplaceholder.typicode.com/todos/"
tasks_res = requests.get(api_url_1)
tasks = tasks_res.json()
api_url_2 = "https://jsonplaceholder.typicode.com/users"
users_res = requests.get(api_url_2)
users = users_res.json()
name = str()
for user in users:
    if user.get("id") == user_no:
        name = user.get("name")
tot_tasks = 0
comp_title = list()
for task in tasks:
    if task.get("userId") == user_no:
        if task.get("completed") is True:
            comp_title.append(task.get("title"))
        tot_tasks += 1
print("Employee {} is done with tasks({}/{}):".format(
      name, len(comp_title), tot_tasks))
for t in comp_title:
    print("\t{}".format(t))
