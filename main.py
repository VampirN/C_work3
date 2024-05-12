import json
from utils import sorted_operations_status
from utils import sorted_operation_date
from utils import message_conversion


def main():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    data = sorted_operations_status(data)
    data = sorted_operation_date(data)

    for i in range(5):
        print(message_conversion(data[i]))
        print()


if __name__ == "__main__":
    main()