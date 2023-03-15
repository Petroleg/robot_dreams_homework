user_input = input("Insert a word or a number: ")
if user_input.isdigit():
    print("You've typed a number.")
    if int(user_input) % 2 == 0:
        print(f"The number {user_input} is even.")
    else:
        print(f"The number {user_input} is odd.")
else:
    print(f"You've typed a word, which length is {len(user_input)} letters")
