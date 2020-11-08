from utilitiees import addToFile
import random
import values

class Drone():
    @staticmethod
    def generate_all():
        data = open("drone.txt", 'r').read().split(',')
        data.pop()

        list = []
        for i in range(values.DRONE_LEN):
            list.append(data[random.randrange(0,values.DRONE_LEN-1)])
        
