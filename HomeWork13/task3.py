from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
class MyCustomException(Exception):
    def __init__(self, message="Custom exception is occurred"):
        super().__init__(message)
        with open("log.txt", "a") as log_file:
            log_file.write(f"{message} at {current_time}\n")
