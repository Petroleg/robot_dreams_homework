from datetime import datetime


def deco_function(times):
    def wrapper(func):

        def inner(*args, **kwargs):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"The name of the function is \"{func.__name__}\" and the time of execution is \"{current_time}\" \n"  * times)
        return inner
    return wrapper
