from utilitiees import addToFile


class ObjectType():
    @staticmethod
    def generate_all():
        data = open("pointtype.txt",'r').read().split(',')
        data.pop()
        addToFile.addToFile('pointtype', ['NamePointType'])

        for index in range(len(data)):
            addToFile.addInstance([index, data[index]])
            if(index != len(data) - 1):
                addToFile.addSeperator()
        addToFile.lastSeperator()

ObjectType.generate_all()
