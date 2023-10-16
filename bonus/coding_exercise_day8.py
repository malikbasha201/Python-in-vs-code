with open("doc.txt","r")as file:
    content = file.read()
    content2 = file.read()
    
print(content2)

#The output of the code will be blank space.
# Because,for the first file.read() the data inside the text file got read.then the cursor will be at the end.
#if you add another read() then it will read from the end.from the end there is a no code except blank space.
#so it will print blank space..