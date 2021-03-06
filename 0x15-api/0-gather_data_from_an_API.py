#!/usr/bin/python3
"""Returns information about his/her TODO list progress"""
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
    for item in all_tasks:
        if item.get("completed") is True:
            number_of_done += 1
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done, number_of_tasks))
    for item in all_tasks:
        if item.get("completed") is True:
            title = item.get("title")
            print("\t {}".format(title))
