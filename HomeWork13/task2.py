from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def decorator_func(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as log_file:
            log_file.write(f"{func.__name__} called at {current_time}\n")
    return wrapper
