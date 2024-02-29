#retrieving employee todo list progress and writing to json

import json
import requests
import sys


employee_id = int(sys.argv[1]) 

#fetching employee general details

employee_details = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_data = employee_details.json()

#fetching employee todo list details

employee_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
todos_details = employee_todos.json()

def todo_list_progress(employee_id):
    
    #fetching employee name
    
    employee_name = employee_data["name"]
    
    #fetching employee total todo list length and completed tasks
    
    total_tasks = len(todos_details)
    completed_tasks = sum(1 for todo in todos_details if todo["completed"])
    
    #printing employee todo list progress      
        
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    for todo in todos_details:
        if todo["completed"]:
            print(f"\t {todo['title']}")
            
def write_to_json(employee_id, employee_name, todos_details):
    #write response to json
    
    response = {str(employee_id): [{"task": todo["title"], "completed": todo["completed"], "username": employee_name} for todo in todos_details]}
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(response, json_file, indent=4)
        
if __name__ == "__main__":   
    todo_list_progress(employee_id)
    write_to_json(employee_id, employee_data["name"], todos_details)
