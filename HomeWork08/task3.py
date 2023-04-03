def uppercaser(element: str) -> str:
    return element.upper()

some_list = list("lowercasestringlist")

for count, item in enumerate(map(uppercaser, some_list)):
    some_list[count] = item
