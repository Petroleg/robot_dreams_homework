import re
import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = input("Please enter file name if format \"file.txt\" ")

with open(file_name) as file:
    content = file.read()

print(content)

expression = re.compile(r"(?P<local_part>([A-Za-z0-9]+[.-_]?)*(?<![.-_]){2,}[A-Za-z0-9]+)@(?P<domain_part>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)")
def replacement(match):
    local_part = match.groupdict()['local_part']
    domain_part = match.groupdict()['domain_part']
    new_string = local_part[0] + "*" * (len(local_part)-1) + "@" + "*" * (len(domain_part)-1) + domain_part[-1]
    return new_string

new_content = expression.sub(replacement, content)

print(new_content)