from utilitiees import addToFile


class ObjectType():
    @staticmethod
    def generate_all():
        data = open("objecttype.txt",'r').read().split(',')
        data.pop()

        listOfList = []
        
        for row in data:
            listOfList.append([row])

        addToFile.addToFile("pointtype", ["NameObjectType"], listOfList)
