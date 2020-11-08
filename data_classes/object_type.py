from utilitiees import addToFile


class ObjectType():
    @staticmethod
    def generate_all():
        data = open("pointtype.txt",'r').read().split(',')
        data.pop()

        listOfList = []
        
        for row in data:
            listOfList.append([row])
