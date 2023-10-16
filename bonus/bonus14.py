from module import parsers14
from module.converter14 import converter


feet_inches = input("Enter feet and inches:")


parsed = parsers14.parse(feet_inches)
result = converter(parsed['feet'],parsed['inches'])

print(f"{parsed['feet']}feet and {parsed['inches']}inches is equal to {result}meters")

if result<1:
    print("kids are too small.")
else:
    print("kids can use slide")