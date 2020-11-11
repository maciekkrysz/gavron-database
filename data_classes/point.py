import values
import random

from utilities import sql_file_utils

class Point():

    @staticmethod
    def generate_all(cursor):
        list = []
        for i in range(values.POINT_LEN):
            list.append([random.randrange(1,values.POINTTYPE_LEN-1),round(random.uniform(values.Wroclaw_Longitude-1,values.Wroclaw_Longitude+1),5),round(random.uniform(values.Wroclaw_Latitude-1,values.Wroclaw_Latitude+1),5)])
       
        sql_file_utils.addToFile("point", ["IdPointType", "Longitude", "Latitude"], list)