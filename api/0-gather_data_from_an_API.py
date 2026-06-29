#!/usr/bin/python3
"""Gather data from an API."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base = "https://jsonplaceholder.typicode.com"

    url_user = "{}/users/{}".format(base, employee_id)
    url_todos = "{}/todos?userId={}".format(base, employee_id)

    with urllib.request.urlopen(url_user) as response:
        user = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(url_todos) as response:
        todos = json.loads(response.read().decode("utf-8"))

    name = user.get("name")
    done = [t for t in todos if t.get("completed") is True]
    total = len(todos)
    num_done = len(done)

    print("Employee {} is done with tasks({}/{}):".format(
        name, num_done, total))
    for task in done:
        print("\t {}".format(task.get("title")))