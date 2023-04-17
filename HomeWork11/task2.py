class MyCustomException(Exception):
    def __init__(self, message="Custom exception is occurred"):
        super().__init__(message)
