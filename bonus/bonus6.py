contents = ["All carrots are to be sliced longitudely",
            "The carrots are reportedly sliced",
            "The slicing process was well presented"]

filenames = ["doc.txt","report.txt","presentation.txt"]

for content,filename in zip(contents,filenames):
    file = open(filename,"w")
    file.write(content)