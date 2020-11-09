from utilities import sql_file_utils
import random
import values


class Drone():
    @staticmethod
    def generate_all():
        data = open("drone.txt", 'r').read().split(',')
        data.pop()

        listOfList = []
        for _ in range(values.DRONE_LEN):
            listOfList.append([data[random.randrange(1, values.DRONE_LEN)]])

        sql_file_utils.addToFile("drone", ["Model"], listOfList)
