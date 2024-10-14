from utils.utils import load_operations
from utils.utils import make_list_of_executed_operations
from utils.utils import output

# if __name__ == "__main__()":

filename = 'operations.json'
data = load_operations(filename)
# print(data)
executed_operations = make_list_of_executed_operations(data)
# print(executed_operations)

new_list = sorted(executed_operations, key=lambda x: x['date'], reverse=True)

# print(new_list)

latest_five = new_list[:5]
# print(latest_five)

for operation in latest_five:
    print(output(operation))
