from utilitiees import addToFile
import values


class ObjectType():
    @staticmethod
    def generate_all():
        data = open("objecttype.txt", 'r').read().split(',')
        data.pop()
        listOfList = []

        for row in data:
            listOfList.append([row])

        values.OBJECTTYPE_LEN = len(data)
        addToFile.addToFile("objectype", ["NameObjectType"], listOfList)
