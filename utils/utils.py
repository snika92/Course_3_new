import json
import datetime


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


def output(operation):
    op_date = operation['date'].split('T')
    # print(op_date[0])
    operation_date = datetime.date.fromisoformat(op_date[0]).strftime("%d.%m.%y")
    if "from" in operation:
        from_ = operation["from"].split()
        from_account = from_.pop()
        star_from_account = f"{from_account[:4]} {from_account[6:8]}** **** {from_account[-4:]}"
        from_card_name = " ".join(from_)
        from_name = f"{from_card_name} {star_from_account}"
    else:
        from_name = "..."

    to_ = operation["to"].split()
    to_account = to_.pop()
    star_to_account = f"**{to_account[-4:]}"
    to_name = " ".join(to_)

    return (f"""{operation_date} {operation['description']}
{from_name} -> {to_name} {star_to_account}
{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}
""")
