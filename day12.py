def get_todos(filepath):
    with open(filepath,"r")as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(filepath,todos_arg):
    with open(filepath,"w")as file:
        file.writelines(todos_arg)


while True:
    user = input("Type add,show,edit,complete or exit :")
    user = user.strip()

    if user.startswith("add"):
        
        mal = user[4:]
        todo = str(mal)+"\n"

        todos = get_todos("todos.txt")

        todos.append(todo)

        write_todos('todos.txt',todos) 
        
    elif user.startswith("show"):
        todos = get_todos("todos.txt")
        
        new_todos = [item.strip('\n')for item in todos]

        for index,item in enumerate(new_todos):
            row = f"{index+1}:-{item}"
            print(row)
    elif user.startswith("edit"):
        try:
            num = user[5:]
            number = int(num)
            print(number)
            number = number-1

            todos = get_todos("todos.txt")

            todo = input("Enter the New todo :")
            todos[number] = todo + '\n'

            write_todos("todos.txt",todos)
        except:
            print("Your code is not valid.")
            continue
    elif user.startswith("complete"):
        try:
            number = int(user[9:])
            num = number-1

            todos = get_todos("todos.txt")

            todo_to_remove = todos[num].strip('\n')
            todos.pop(num)

            write_todos("todos.txt",todos)
            
            message = f"todo {todo_to_remove} was removed from the list"
            print(message)
        except:
            print("There is no item with that number")
            continue

    elif user.startswith("exit"):
        break
    else:
        print("Hey!You entered the wrong one...")
print("Bye!")