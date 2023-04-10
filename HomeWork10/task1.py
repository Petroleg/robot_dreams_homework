def recursive_function(number: int) -> None:
    print(number)
    if number == 0:
        return None
    return recursive_function(number - 1)
