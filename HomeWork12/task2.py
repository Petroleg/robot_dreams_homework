class MyManager:
    def __enter__(self):
        print("="*10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("="*10)
        if isinstance(exc_val, Exception):
            print(f"An exception occurred: {exc_type}")
            print(f"Exception message: {exc_val}")
            return True
