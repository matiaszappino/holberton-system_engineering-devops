#!/usr/bin/python3
"""Returns information about his/her TODO list progress"""
import requests
import sys
import csv


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
    for item in all_tasks:
        with open("{}.csv".format(user_id), mode="w") as file:
            file = csv.writer(
                file, delimiter=",", quoting=csv.QUOTE_ALL)
            file.writerow([user_id, employee_name, item.get(
                    "completed"), item.get("title")])
