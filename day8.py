

while True:
    user = input("Type add,show,edit,complete or exit :")
    user = user.strip()

    match user:
        case "add":
            mal = input("Enter the name to add :") + "\n"
                       
            with open("todos.txt","r")as file:
                todos = file.readlines()

            todos.append(mal)

            with open("todos.txt","w")as file:
                file.writelines(todos)
        case "show":
            with open("todos.txt","r")as file:
                todos = file.readlines()
            
            new_todos = [item.strip('\n')for item in todos]

            for index,item in enumerate(new_todos):
                row = f"{index+1}:-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the Number of the todo to edit :"))
            number = number-1

            with open("todos.txt","r")as file:
                todos = file.readlines()

            todo = input("Enter the New todo :")
            todos[number] = todo + '\n'

            with open("todos.txt","w")as file:
                file.writelines(todos)
        case "complete":
            num = int(input("Enter the Number to complete :"))
            num = num-1

            with open("todos.txt","r")as file:
                todos = file.readlines()

            todo_to_remove = todos[num].strip('\n')
            todos.pop(num)

            with open("todos.txt","w")as file:
                file.writelines(todos)
            message = f"todo {todo_to_remove} was removed from the list"
            print(message)

        case "exit":
            break
        case x:
            print("Hey!You entered the wrong one...")

print("Bye!")