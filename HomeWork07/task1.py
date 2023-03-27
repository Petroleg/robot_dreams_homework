phone_book = {}

while True:
    command_name_phone = input('Pick one command: "stats" "add" "list" "delete <name>" "show <name>" . ').split()
    if len(command_name_phone) > 0:
        command = command_name_phone[0]
    else:
        print("You have to enter a command. ")
        continue

    if command == "stats":
        print(f"Your phone book has {len(phone_book)} contacts.")
    elif command == "list":
        if len(phone_book) > 0:
            for contact in phone_book.keys():
                print(contact)
        else:
            print("Nothing to show at the moment, add some contacts.")
    elif command == "show":
        name = command_name_phone[1]
        print(phone_book.get(name,"Name not in your phone_book. Use command \"list\" and try again."))
    elif command == "add":
        name = command_name_phone[1]
        phone = command_name_phone[2]
        if name not in phone_book.keys():
            phone_book[name] = phone
        else:
            print(f"{name} is already in your phone book. Use command \"list\" and try again.")
    elif command == "delete":
        name = command_name_phone[1]
        if name in phone_book.keys():
            del phone_book[name]
        else:
            print("There's no such contact in your phone book. Use command \"list\" and try again.")
    else:
        print("Wrong command, please try again!")
