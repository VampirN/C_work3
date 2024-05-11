import json
from utils import sorted_operations
from utils import message_conversion


def main():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    items = sorted_operations(data)

    for i in range(5):
        print(message_conversion(items[i]))
        print()


if __name__ == "__main__":
    main()