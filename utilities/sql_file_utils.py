from values import SCRIPT_FILENAME


def addEntityDeclaration(entity, listOfAtributes):

    filepath = SCRIPT_FILENAME
    file = open(filepath, "a", encoding="utf-8")

    file.write("INSERT INTO " + entity + "( ")
    for k in range(len(listOfAtributes)):
        if(k == len(listOfAtributes)-1):
            file.write(listOfAtributes[k] + "")
        else:
            file.write(listOfAtributes[k] + ", ")
    file.write(" )" + " VALUES ")
    file.close()


def addInstance(listOfValues):

    filepath = SCRIPT_FILENAME
    file = open(filepath, "a", encoding="utf-8")
    file.write("(")
    for k in range(len(listOfValues)):
        if(k == len(listOfValues) - 1):
            file.write("'"+str(listOfValues[k]) + "'")
        else:
            file.write("'"+str(listOfValues[k]) + "', ")
    file.write(")")
    file.close()


def addToFile(entity, listOfAttributes, listOfAllValueLists):
    addEntityDeclaration(entity, listOfAttributes)

    file = open(SCRIPT_FILENAME, "a", encoding="utf-8")

    for index in range(len(listOfAllValueLists)):
        if index % 2000 == 0:
            file.write(';\n')
            addEntityDeclaration(entity, listOfAttributes)

        addInstance(listOfAllValueLists[index])
        if (index != len(listOfAllValueLists) - 1):
            addSeperator()
    lastSeperator()

    file.write("\n")
    file.close()


def addSeperator():
    filepath = SCRIPT_FILENAME
    file = open(filepath, "a", encoding="utf-8")
    file.write(",\n")


def lastSeperator():
    filepath = SCRIPT_FILENAME
    file = open(filepath, "a", encoding="utf-8")
    file.write(";\n")
