#from functions import get_todos,write_todos

import functions
import time

now = time.strftime("%B %d , %Y %H:%M:%S")
print("it is ",now)

while True:
    user = input("Type add,show,edit,complete or exit :")
    user = user.strip()

    if user.startswith("add"):
        
        mal = user[4:]
        todo = str(mal)+"\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos) 
        
    elif user.startswith("show"):
        todos = functions.get_todos()
        
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

            todos = functions.get_todos()

            todo = input("Enter the New todo :")
            todos[number] = todo + '\n'

            functions.write_todos(todos)
        except:
            print("Your code is not valid.")
            continue
    elif user.startswith("complete"):
        try:
            number = int(user[9:])
            num = number-1

            todos = functions.get_todos()

            todo_to_remove = todos[num].strip('\n')
            todos.pop(num)

            functions.write_todos(todos)
            
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