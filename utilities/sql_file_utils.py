from values import SCRIPT_FILENAME


def addEntityDeclaration(entity, listOfAtributes, ignore):
    ret_str = "INSERT "
    if ignore:
        ret_str += "IGNORE "
    ret_str += "INTO " + entity + "( "
    for k in range(len(listOfAtributes)):
        if(k == len(listOfAtributes)-1):
            ret_str += listOfAtributes[k] + ""
        else:
            ret_str += listOfAtributes[k] + ", "
    ret_str += " )" + " VALUES "
    return ret_str


def addInstance(listOfValues):
    ret_str = ""
    ret_str += '('
    for k in range(len(listOfValues)):
        if(k == len(listOfValues) - 1):
            ret_str += "'" + str(listOfValues[k]) + "'"
        else:
            ret_str += "'" + str(listOfValues[k]) + "', "
    ret_str += ')'
    return ret_str


def addToFile(cursor, entity, listOfAttributes, listOfAllValueLists, ignore=False):
    ret_str = ""
    ret_str += addEntityDeclaration(entity, listOfAttributes, ignore)

    for index in range(len(listOfAllValueLists)):
        ret_str += addInstance(listOfAllValueLists[index])
        if index % 2000 == 0 and index > 0:
            ret_str += lastSeperator()
            cursor.execute(ret_str)
            ret_str = addEntityDeclaration(entity, listOfAttributes, ignore)
        elif(index != len(listOfAllValueLists) - 1):
            ret_str += addSeperator()
    ret_str += lastSeperator()
    cursor.execute(ret_str)
    return ret_str


def addSeperator():
    return ',\n'


def lastSeperator():
    return ';'
