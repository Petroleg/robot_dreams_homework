class MyCustomException(Exception):
    def __init__(self, message="Custom exception is occurred"):
        self.message = message
        super().__init__(self.message)
