FILEPATH = "todos.txt"

def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

