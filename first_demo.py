with open("demo.txt" , "r") as reader:
    lines = reader.readlines()
    newlist = lines[::-1]
    with open("demo.txt" ,'w') as writer:
        for line in newlist:
            writer.write(line)


