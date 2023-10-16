feet_inches = input("Enter feet and inches: ")


def converter(feet):
    parts = feet.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters

result = converter(feet_inches)

if result < 1:
    print("kids are too small to paly the slide")
else:
    print("kids can play the slide")