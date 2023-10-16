'''from fileinput import filename


filename = ["1.Raw DAta.txt","2.Reports.txt","3.Presentation.txt"]

for i in filename:
    i = i.replace('.','-',1)
    print(i)'''



'''m = ['a','b','c','d']

for i,j in enumerate(m):
    row = f"{i}:{j}"
    print(row)'''

a = enumerate(["a",'b','c'])

print(tuple(a))
