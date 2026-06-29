#!/usr/bin/python3
"""Script that fetches employee TODO list progress from a REST API."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(f"{base_url}/users/{employee_id}") as r:
        user = json.loads(r.read().decode())

    with urllib.request.urlopen(
        f"{base_url}/todos?userId={employee_id}"
    ) as r:
        todos = json.loads(r.read().decode())

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    total = len(todos)
    done = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({done}/{total}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")