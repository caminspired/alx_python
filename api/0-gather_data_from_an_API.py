#Script to fetche employee todo list progress

import requests
import sys


def todo_list_progress(employee_id):
    
    #fetching employee details
    
    employee_details = requests.get("https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_details.json()
    employee_name = employee_data['name']        
    todos = len(employee_todos)
    
    #fetching employee todos
    
    employee_todos = requests.get("https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_details = employee_todos.json()
    total_tasks = len(employee_details)
    completed_tasks = 0
    
    for todo["completed"] in todos:
        completed_tasks +1
        
    #printing employee todo list progress          
    
    print("Employee {} is done with tasks{}/{}".format(employee_name, completed_tasks, total_tasks))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
        
    todo_list_progress(employee_id)
    employee_id = int(sys.argv[1])
