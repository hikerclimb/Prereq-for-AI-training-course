import json

try:
    file='input.txt'
    with open(file, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found')
try:
    with open('MalformedJson.json', 'r') as file:
        data = json.load(file)

    # 'data' is now a Python dictionary or list
    print(data)
except json.JSONDecodeError as e:
    print(f"Failed to parse JSON!")
    print(f"Error Message: {e.msg}")
    print(f"Line number: {e.lineno}")
    print(f"Column number: {e.colno}")
