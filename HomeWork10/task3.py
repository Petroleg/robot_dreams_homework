def factorial(number):
    if number in {0, 1}:
        return 1
    return number * factorial(number - 1)
