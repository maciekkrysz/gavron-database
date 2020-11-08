def addToFile(entity, listOfAtributes, listOfValues):

    filepath = "plik.txt"
    file = open(filepath, "a", encoding="utf-8")

    file.write("INSERT INTO " +entity + "( ")
    for k in range(len(listOfAtributes)):
        if(k == len(listOfAtributes)-1):
            file.write(listOfAtributes[k] + "")
        else:
            file.write(listOfAtributes[k] + ", ")
    file.write(" )" + " VALUES (")

    for k in range(len(listOfValues)):
        if(k == len(listOfValues) -1):
            file.write("'"+listOfValues[k] + "'")
        else:
            file.write("'"+listOfValues[k] + "', ")
    file.write(" );\n")
