todo = input("Enter the new member :")

file = open("members.txt",'r')
todos = file.readlines()
file.close()

todos.append(todo + "\n")

file = open("members.txt","w")
file.writelines(todos)
file.close()
