import json


def load_operations(filename):
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
    return data


# operations = load_operations('../src/operations.json')
# print(operations)
