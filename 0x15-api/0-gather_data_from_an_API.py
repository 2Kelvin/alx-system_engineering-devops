#!/usr/bin/python3
"""Module gather data from an API"""

if __name__ == '__main__':
    import requests
    from sys import argv

    EMPLOYEE_NAME = ''
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    employeeId = int(argv[1])

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    for userDict in users.json():
        if userDict['id'] == employeeId:
            EMPLOYEE_NAME = userDict.get('name')
            break

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for todo in todos.json():
        if todo['userId'] == employeeId:
            if todo['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo.get('title'))
            TOTAL_NUMBER_OF_TASKS += 1

    firstLine = 'Employee {} is done with tasks'.format(EMPLOYEE_NAME)
    secondLine = '({}/{}):'.format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
    print(f'{firstLine}{secondLine}')
    for title in TASK_TITLE:
        print(f'     {title}')
