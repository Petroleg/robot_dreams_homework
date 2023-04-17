phone_book = {}

while True:
    command_name_phone = input('Pick one command: "stats" "add" "list" "delete <name>" "show <name>" . ').split()
    if len(command_name_phone) > 0:
        command = command_name_phone[0]
    else:
        print("You have to enter a command. ")
        continue

    def stats(phone_book_dict) -> None:
        print(f"Your phone book has {len(phone_book_dict)} contacts.")


    def lst(phone_book_dict):
        if len(phone_book_dict) > 0:
            for contact in phone_book_dict.keys():
                print(contact)
        else:
            print("Nothing to show at the moment, add some contacts.")


    def show(phone_book_dict, command_name_phone_list):
        if len(command_name_phone_list) > 1:
            name = command_name_phone_list[1]
            print(phone_book_dict.get(name, f"\"{name}\" not in your phone_book. Use command \"list\" and try again."))
        else:
            print("Nothing to show at the moment, add some contacts.")


    def add(phone_book_dict, command_name_phone_list):
        name = command_name_phone_list[1]
        try:
            phone = command_name_phone_list[2]
        except IndexError:
            print("Your command should look like: \"add Oleh +123456789\". Some elements are missing, try again!")
        else:
            if name not in phone_book.keys():
                phone_book_dict[name] = phone
            else:
                print(f"{name} is already in your phone book. Use command \"list\" and try again.")


    def delete(phone_book_dict, command_name_phone_list):
        name = command_name_phone_list[1]
        try:
            del phone_book_dict[name]
        except KeyError:
            print("There's no such contact in your phone book. Use command \"list\" and try again.")


    if command == "stats":
        stats(phone_book)
    elif command == "list":
        lst(phone_book)
    elif command == "show":
        show(phone_book, command_name_phone)
    elif command == "add":
        add(phone_book, command_name_phone)
    elif command == "delete":
        delete(phone_book, command_name_phone)
    else:
        print("Wrong command, please try again!")
