feet_inches = input("Enter feet and inches:")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    return {"feet":feet,"inches":inches}

def converter(feet,inches):
    meters = feet * 0.3048 + inches *0.254
    return meters

parsed = parse(feet_inches)
result = converter(parsed['feet'],parsed['inches'])

print(f"{parsed['feet']}feet and {parsed['inches']}inches is equal to {result}meters")

if result<1:
    print("kids are too small.")
else:
    print("kids can use slide")