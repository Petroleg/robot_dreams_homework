def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


fib_number = int(input("Please enter a number in Fibonacci sequence you would like to know: "))

print(fibonacci(fib_number))
