class Warehouse:
    items = {
        "name": "",
        "quantity": "",
        "unit": "",
        "unit_price": ""
    }


def main():
    print('Welcome to Warehouse Management')
    print('Usage: items, add, del, exit')
    print('')

    while True:
        command = input("Operation: ")
        print('')

        match command:
            case "exit":
                exit(0)
            case "items":
                print('items')
            case "add":
                print('add')
            case "del":
                print("del")
            case _:
                print("There's no such thing")

        print('')


if __name__ == "__main__":
    main()
