user_input = input("Insert a word or a number: ")
match user_input:
    case str() if user_input.isdigit() and int(user_input) % 2 == 0:
        print(f"You've entered a number {user_input}.\nThe number {user_input} is even.")
    case str() if user_input.isdigit():
        print(f"You've entered a number {user_input}.\nThe number {user_input} is odd.")
    case str():
        print(f"You've typed a word, which length is {len(user_input)} letters")
    case _:
        print("You have entered something that is not a string or an integer, for example a sequence. I think we can also handle it here if we check user_input[0] and user_input[-1] elements for being '[', ']', '(',')', etc... ")