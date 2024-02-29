import requests
import sys


def todo_list_progress(employee_id):
    
    #fetching employee details
    
    employee_details = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_details.json()
    employee_name = employee_data["name"]
    
    #fetching employee todos
    
    employee_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todos_details = employee_todos.json()
    total_tasks = len(todos_details)
    completed_tasks = sum(1 for todo in todos_details if todo["completed"])
    
    #printing employee todo list progress          
    
    print("Employee {} is done with tasks{}/{}".format(employee_name, completed_tasks, total_tasks))

    for idx, todo in enumerate(todos_details, start=1):
        if todo["completed"]:
            print(f"\t{todo['title']}")
    
if __name__ == "__main__":
    employee_id = int(sys.argv[1])    
    todo_list_progress(employee_id)

