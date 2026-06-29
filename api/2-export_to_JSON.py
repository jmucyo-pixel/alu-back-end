#!/usr/bin/python3
"""Export employee TODO list data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base), params={"userId": employee_id}
    ).json()

    username = user.get("username")
    filename = "{}.json".format(employee_id)

    data = {str(employee_id): [
        {
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        }
        for t in todos
    ]}

    with open(filename, "w") as f:
        json.dump(data, f)