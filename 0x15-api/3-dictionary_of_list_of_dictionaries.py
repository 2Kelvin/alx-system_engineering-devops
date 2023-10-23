#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

if __name__ == '__main__':
    import requests

    EMPLOYEE_NAME = ''
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    USERNAME = ''

    def getUsername(userId):
        """Get the USERNAME from api"""
        users = requests.get('https://jsonplaceholder.typicode.com/users')
        alias = ''
        for userDict in users.json():
            if userDict['id'] == userId:
                alias = userDict.get('username')
                break
        return alias

    employeeId = 1

    with open('todo_all_employees.json', 'w', encoding='UTF8') as userjsonFile:
        userjsonFile.write('{')

        while employeeId < 11:
            USERNAME = getUsername(employeeId)

            todos = requests.get('https://jsonplaceholder.typicode.com/todos')
            TASK_TITLE = []
            for todo in todos.json():
                if todo['userId'] == employeeId:
                    s = f'"completed": {str(todo.get("completed")).lower()}'
                    TASK_TITLE.append(
                        f'{{"username": "{USERNAME}", \
                            "task": "{todo.get("title")}", {s}}}'
                    )

            userjsonFile.write(f'"{employeeId}": [')
            if employeeId == 10:
                for eachData in TASK_TITLE:
                    if eachData == TASK_TITLE[-1]:
                        userjsonFile.write(
                            f'{eachData}]'
                        )
                    else:
                        userjsonFile.write(
                            f'{eachData}, '
                        )
            else:
                for eachData in TASK_TITLE:
                    if eachData == TASK_TITLE[-1]:
                        userjsonFile.write(
                            f'{eachData}], '
                        )
                    else:
                        userjsonFile.write(
                            f'{eachData}, '
                        )

            employeeId += 1

        userjsonFile.write('}')
