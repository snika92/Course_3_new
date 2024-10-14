import json


def load_operations(filename):
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
    return data


operations = load_operations('../src/operations.json')
# print(operations)


def make_list_of_executed_operations(data):
    list_of_executed_operations = []
    for operation in data:
        if operation:
            if operation['state'] == 'EXECUTED':
                list_of_executed_operations.append(operation)
    return list_of_executed_operations


executed_operations = make_list_of_executed_operations(operations)
# print(executed_operations)


