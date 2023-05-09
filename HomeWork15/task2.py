import re
import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = input("Please enter file name if format \"file.txt\" ")

with open(file_name) as file:
    content = file.read()

print(content)

expression = re.compile(r"([A-Za-z0-9]+[.-_]?)*(?<![.-_]){2,}[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
content = re.sub(expression, "*@*", content)

print(content)

