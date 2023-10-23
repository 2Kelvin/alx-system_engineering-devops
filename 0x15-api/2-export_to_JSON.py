#!/usr/bin/python3
"""Export to JSON"""

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
            complte = f'"completed": {str(todo.get("completed")).lower()}'
            TASK_TITLE.append(
                f'{{"task": "{todo.get("title")}", {complte}, \
                    "username": "{USERNAME}"}}'
            )

    with open(f'{employeeId}.json', 'w', encoding='UTF8') as userjsonFile:
        userjsonFile.write(
            f'{{"{employeeId}": ['
        )

    with open(f'{employeeId}.json', 'a', encoding='UTF8') as userjsonFile1:
        for eachData in TASK_TITLE:
            if eachData == TASK_TITLE[-1]:
                userjsonFile1.write(
                    f'{eachData}'
                )
            else:
                userjsonFile1.write(
                    f'{eachData}, '
                )

    with open(f'{employeeId}.json', 'a', encoding='UTF8') as userjsonFile2:
        userjsonFile2.write(
            f']}}'
        )
