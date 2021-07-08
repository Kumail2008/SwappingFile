def swapFileData():
    print("This is a file swapper")
    file1=input("Enter file 1: ")
    file2=input("Enter file 2: ")

    data_a = open(file1,"r")
    data_b = open(file2,"r")

    file1NewContent = data_b.read()
    file2NewContent = data_a.read()
    
    data_a.close()
    data_b.close()

    data_a = open(file1,"w")
    data_b = open(file2,"w")

    data_a.write(file1NewContent)
    data_b.write(file2NewContent)
    
    data_a.close()
    data_b.close()

    data_a = open(file1,"r")
    data_b = open(file2,"r")

    print("File 1's new content: ")
    print(data_a.read())
    print("File 2's new content: ")
    print(data_b.read())

swapFileData()   
