user_input = input("Please enter something: ")
for element in user_input:
    if element.isdigit():
        if int(element) % 2 == 0:
            print(f"{element} is an even number!")
        else:
            print(f"{element} is an odd number!")
    elif element.isalpha():
        if element.isupper():
            print(f"{element} is an uppercase letter!")
        else:
            print(f"{element} is a lowercase letter!")
    else:
        print(f"{element} is an ASCII symbol!")
