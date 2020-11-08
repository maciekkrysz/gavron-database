import values
import random

class Point():

    @staticmethod
    def generate_all():
        list = []
        for i in range(values.POINT_LEN):
            list.append([random.randrange(1,values.POINTTYPE_LEN),random.randrange(values.Wroclaw_Longitude-5,values.Wroclaw_Longitude+5),random.randrange(values.Wroclaw_Latitude-5,values.Wroclaw_Latitude+5)])
        print(list)

