#JSON JavaScript Object Notation
import json

with open('works_with_json.json', 'r') as file:
    data = json.load(file)

print(data)