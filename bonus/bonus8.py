date = input("Enter today's date:")
mood = input("How do you rate your mood today from 1 t0 10?")
thoughts = input("Let your thoughts flow:\n")

with open(f"{date}.txt","w")as file:
    file.writelines(mood+3*"\n")
    file.writelines(thoughts)

