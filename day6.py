

while True:
    user = input("Type add,show,edit,complete or exit :")
    user = user.strip()

    match user:
        case "add":
            mal = input("Enter the name to add :") + "\n"
           
            file = open("todos.txt","r")
            todos = file.readlines()
            file.close()

            todos.append(mal)

            file = open("todos.txt","w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("todos.txt","r")
            todos = file.readlines()
            file.close()
            
            new_todos = [item.strip('\n')for item in todos]

            for index,item in enumerate(new_todos):
                row = f"{index+1}:-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the Number of the todo to edit :"))
            number = number-1
            todo = input("Enter the New todo :")
            new_todos[number] = todo
        case "complete":
            num = int(input("Enter the Number to complete :"))
            num = num-1
            new_todos.pop(num)
        case "exit":
            break
        case x:
            print("Hey!You entered the wrong one...")

print("Bye!")