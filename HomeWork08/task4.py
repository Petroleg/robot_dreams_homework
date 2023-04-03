a_list = [1, 2, 3.4, "six", [7,8], "somestring", 122.3, 9, 11, 10]

numbers  = filter(lambda a: str(a).isdigit(), a_list)
for number in numbers:
    print(number)
