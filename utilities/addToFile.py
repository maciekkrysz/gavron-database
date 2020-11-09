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


def addToFile(entity, listOfAttributes, listOfAllValueLists):
    addEntityDeclaration(entity, listOfAttributes)

    for index in range(len(listOfAllValueLists)):
        addInstance(listOfAllValueLists[index])
        if (index != len(listOfAllValueLists) - 1):
            addSeperator()
    lastSeperator()


def addSeperator():
    filepath = SCRIPT_FILENAME
    file = open(filepath, "a", encoding="utf-8")
    file.write(",\n")


def lastSeperator():
    filepath = SCRIPT_FILENAME
    file = open(filepath, "a", encoding="utf-8")
    file.write(";\n")
