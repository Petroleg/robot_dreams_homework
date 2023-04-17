from datetime import datetime


def deco_function(func):
    def wrapper(*args, **kwargs):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"The name of the function is \"{func.__name__}\" and the time of execution is \"{current_time}\"")
    return wrapper
