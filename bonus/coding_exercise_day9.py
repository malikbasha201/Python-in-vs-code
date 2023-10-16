

while True:
    user = input("Type add,show,edit,complete or exit :")
    user = user.strip()

    if "add" in user or 'new' in user:
        
        mal = user[4:]
        todo = str(mal)+"\n"

        with open("todos.txt","r")as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt","w")as file:
            file.writelines(todos)
    elif "show" in user:
        with open("todos.txt","r")as file:
            todos = file.readlines()
        
        new_todos = [item.strip('\n')for item in todos]

        for index,item in enumerate(new_todos):
            row = f"{index+1}:-{item}"
            print(row)
    elif "edit" in user:
        num = user[5:]
        number = int(num)
        print(number)
        number = number-1

        with open("todos.txt","r")as file:
            todos = file.readlines()

        todo = input("Enter the New todo :")
        todos[number] = todo + '\n'

        with open("todos.txt","w")as file:
            file.writelines(todos)
    elif "complete" in user:
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

    elif "exit" in user:
        break
    else:
        print("Hey!You entered the wrong one...")
print("Bye!")