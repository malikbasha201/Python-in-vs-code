todos = []

while True:
    user = input("Type add,show,edit,complete or exit: ")
    user = user.strip()
    
    match user:
        case "add":
            new_todo = input("Enter the todo to add: ")
            todos.append(new_todo)
        case "show":
            for index,item in enumerate(todos):
                print(f"{index+1}:-{item}")
                
        case "edit":
            user_edit = int(input("Enter the Number of the todo to edit: "))
            new_edit = input("Enter the new todo: ")
            todos[user_edit] = new_edit
            
        case "complete":
            to_delete = int(input("Enter the No.of the todo to complete: "))
            todos.pop(to_delete-1)
            
        case "exit":
            break
        case x:
            print("Hey!You entered the wrong one bro....")
            
print("Bye...")