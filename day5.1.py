todos = []

while True:
    user = input("Type add,show,edit,complete or exit :")
    user = user.strip()

    match user:
        case "add":
            mal = input("Enter the Name to add :")
            todos.append(mal)
        case "show":
            for index,item in enumerate(todos):
                '''print(index,':',item)
                        or          '''
                row = f"{index+1}:-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the number to edit:"))
            number = number-1
            todo = input("Enter the new todo :")
            todos[number] = todo
        case "complete":
            num = int(input("Enter the Number of todo to complete :"))
            todos.pop(num-1)
        case "exit":
            break
        case x:
            print("Hey!you entered the wrong one....")
print("Bye!")