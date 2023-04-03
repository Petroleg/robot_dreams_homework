phone_book = {}

while True:
    command_name_phone = input('Pick one command: "stats" "add" "list" "delete <name>" "show <name>" . ').split()
    if len(command_name_phone) > 0:
        command = command_name_phone[0]
    else:
        print("You have to enter a command. ")
        continue

    def stats() -> None:
        print(f"Your phone book has {len(phone_book)} contacts.")


    def lst(phone_book=phone_book):
        if len(phone_book) > 0:
            for contact in phone_book.keys():
                print(contact)
        else:
            print("Nothing to show at the moment, add some contacts.")


    def show(phone_book=phone_book, command_name_phone=command_name_phone):
        if len(command_name_phone) > 1:
            name = command_name_phone[1]
            print(phone_book.get(name, f"\"{name}\" not in your phone_book. Use command \"list\" and try again."))
        else:
            print("Nothing to show at the moment, add some contacts.")

    def add(phone_book=phone_book, command_name_phone=command_name_phone):
        name = command_name_phone[1]
        phone = command_name_phone[2]
        if name not in phone_book.keys():
            phone_book[name] = phone
        else:
            print(f"{name} is already in your phone book. Use command \"list\" and try again.")


    def delete(phone_book=phone_book, command_name_phone=command_name_phone):
        name = command_name_phone[1]
        if name in phone_book.keys():
            del phone_book[name]
        else:
            print("There's no such contact in your phone book. Use command \"list\" and try again.")


    if command == "stats":
        stats()
    elif command == "list":
        lst()
    elif command == "show":
        show()
    elif command == "add":
        add()
    elif command == "delete":
        delete()
    else:
        print("Wrong command, please try again!")
