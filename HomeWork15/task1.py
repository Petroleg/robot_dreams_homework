import os
import json
import re


def load_phone_book():
    if os.path.exists("phone_book.json") and os.stat("phone_book.json").st_size != 0:
        with open("phone_book.json", 'r') as json_file:
            return json.load(json_file)
    return {}


def save_phone_book(phone_book):
    with open("phone_book.json", "w") as file:
        json.dump(phone_book, file)


def show_stats(phone_book):
    print(f"Your phone book has {len(phone_book)} contacts.")


def show_all_contacts(phone_book):
    if len(phone_book) > 0:
        for contact in phone_book:
            print(contact)
    else:
        print("Nothing to show at the moment, add some contacts.")


def show_contact(phone_book, name):
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"\"{name}\" not in your phone book. Use command \"list\" and try again.")


def add_contact(phone_book, name, phone):
    if name not in phone_book:
        expression = re.compile(r"(?P<prefix>(?:^\+?380|80|0))(?P<operator>(?:39|50|6[3,6-8]|73|89|9[1-9]))(?P<number>\d{7}$)") #написав сам таку штуку страшну, хотілось би коментар, як її можна заімпрувити)
        valid = expression.match(phone)
        if valid:
            print(f"Number {valid.group()} added successfully")
            phone_book[name] = phone
        else:
            print(f"Phone has to be a valid ukrainian phone number, not {phone}")
    else:
        print(f"{name} is already in your phone book. Use command \"list\" and try again.")


def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
    else:
        print("There's no such contact in your phone book. Use command \"list\" and try again.")


phone_book = load_phone_book()

while True:
    command = input('Pick one command: "stats" "add" "list" "delete <name>" "show <name>" . ').split()
    if not command:
        print("You have to enter a command. ")
        continue

    if command[0] == "stats":
        show_stats(phone_book)

    elif command[0] == "list":
        show_all_contacts(phone_book)

    elif command[0] == "show":
        if len(command) > 1:
            show_contact(phone_book, command[1])
        else:
            print("You have to specify the contact name to show.")

    elif command[0] == "add":
        if len(command) < 3:
            print("Your command should look like: \"add Oleh +123456789\". Some elements are missing, try again!")
        else:
            add_contact(phone_book, command[1], command[2])
            save_phone_book(phone_book)

    elif command[0] == "delete":
        if len(command) < 2:
            print("You have to specify the contact name to delete.")
        else:
            delete_contact(phone_book, command[1])
            save_phone_book(phone_book)

    else:
        print("Wrong command, please try again!")
