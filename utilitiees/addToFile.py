def addEntityDeclaration(entity, listOfAtributes):

    filepath = "plik.txt"
    file = open(filepath, "a", encoding="utf-8")

    file.write("INSERT INTO " +entity + "( ")
    for k in range(len(listOfAtributes)):
        if(k == len(listOfAtributes)-1):
            file.write(listOfAtributes[k] + "")
        else:
            file.write(listOfAtributes[k] + ", ")
    file.write(" )" + " VALUES ")

def addInstance(listOfValues):

    filepath = "plik.txt"
    file = open(filepath, "a", encoding="utf-8")
    file.write("(")
    for k in range(len(listOfValues)):
        if(k == len(listOfValues) -1):
<<<<<<< HEAD
            file.write("'"+listOfValues[k] + "'")
=======
            file.write("('"+str(listOfValues[k]) + "'")
>>>>>>> 6112e92... user
        else:
            file.write("'"+str(listOfValues[k]) + "', ")
    file.write(")")

def addToFile(entity, listOfAttributes, listOfAllValueLists):
    addEntityDeclaration(entity, listOfAttributes)

    for index in range(len(listOfAllValueLists)):
        addInstance(listOfAllValueLists[index])
        if (index != len(listOfAllValueLists) - 1):
            addSeperator()
    lastSeperator()

def addSeperator():
    filepath = "plik.txt"
    file = open(filepath, "a", encoding="utf-8")
    file.write(",\n")

def lastSeperator():
    filepath = "plik.txt"
    file = open(filepath, "a", encoding="utf-8")
    file.write(";\n")