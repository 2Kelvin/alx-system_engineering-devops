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
    USERNAME = ''

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    for userDict in users.json():
        if userDict['id'] == employeeId:
            EMPLOYEE_NAME = userDict.get('name')
            USERNAME = userDict.get('username')
            break

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    for todo in todos.json():
        if todo['userId'] == employeeId:
            TASK_TITLE.append({todo.get('completed'): todo.get('title')})

    with open(f'{employeeId}.csv', 'w', encoding='UTF8') as usercsvFile:
        for eachDict in TASK_TITLE:
            for status, title in eachDict.items():
                usercsvFile.write(
                    f'"{employeeId}","{USERNAME}","{status}","{title}"\n'
                )
