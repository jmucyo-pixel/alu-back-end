#!/usr/bin/python3
"""Export all employees TODO data to a single JSON file."""
import json
import requests


if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base)).json()
    todos = requests.get("{}/todos".format(base)).json()
    data = {}
    for user in users:
        uid = user.get("id")
        username = user.get("username")
        data[str(uid)] = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
            }
            for t in todos if t.get("userId") == uid
        ]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
