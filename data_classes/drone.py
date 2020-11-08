from utilitiees import addToFile
import random
import values


class Drone():
    @staticmethod
    def generate_all():
        data = open("drone.txt", 'r').read().split(',')
        data.pop()

        listOfList = []
        for i in range(values.DRONE_LEN):
            listOfList.append([data[random.randrange(1, values.DRONE_LEN)]])

        addToFile.addToFile("drone", ["ModelName"], listOfList)
