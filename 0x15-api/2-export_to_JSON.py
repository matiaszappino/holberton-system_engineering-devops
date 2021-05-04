#!/usr/bin/python3
"""Returns information about his/her TODO list progress"""
import json
import requests
import sys



if __name__ == "__main__":
    user_id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com/"
    employee_name = (requests.get(api + "users/{}".format(
        user_id)).json()).get("name")
    number_of_tasks = len(requests.get(
        api + "todos/", params={"userId": user_id}).json())
    all_tasks = requests.get(
        api + "todos/", params={"userId": user_id}).json()
    number_of_done = 0
    username = (requests.get(api + "users/{}".format(
        user_id)).json()).get("username")
    for item in all_tasks:
        if item.get("completed") is True:
            number_of_done += 1
    data = {}
    data[user_id] = []
    for item in all_tasks:
        data[user_id].append(
            {"task": item.get("title"), "completed": item.get(
                "completed"), "username": username})
        with open("{}.json".format(user_id), "w") as file:
            json.dump(data, file)
