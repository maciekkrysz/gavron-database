from utilitiees import addToFile


class Role():
    @staticmethod
    def generate_all():
        data = open("drone.txt", 'r').read().split(',')
        data.pop()

        listOfList = []

        for row in data:
            listOfList.append([row])
