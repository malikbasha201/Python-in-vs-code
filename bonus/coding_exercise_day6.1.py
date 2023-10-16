filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for i in filenames:
    file = open(i,"w")
    todos = "Hello"
    file.write(todos)
    file.close()