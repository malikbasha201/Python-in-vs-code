todos = []

while True:
    user_txt = input("Type add,show,edit or exit :")
    user_txt = user_txt.strip()

    match user_txt:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for items in todos:
                print(items)
        case 'edit':
            number = int(input("Enter the number of the todo to edit :"))
            number = number-1
            new_todo = input("Enter new todo:")
            todos[number] = new_todo
            
        case 'exit':
            break
        case x:
            print("Hey,you entered an unknown command")
print("Bye !")