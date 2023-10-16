def get_average(fileway):
    with open(fileway,"r") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i)for i in values]
    return values

average = get_average("data.txt")

total = sum(average)/len(average)

print(total)