try:  
    length = float(input("Enter the length of the rectangle:"))
    width = float(input("Enter the width of the rectangle:"))

    if length==width:
        exit("That looks like a square")
    area = length*width

    print(area)
except ValueError:
    print("please Enter the number in digits:")