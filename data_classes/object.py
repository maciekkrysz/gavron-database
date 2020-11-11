from utilities import sql_file_utils
import values
import random


class Object():
    @staticmethod
    def generate_all(cursor):
        lista = []
        for i in range(values.OBJECT_LEN):
            link = "/" + str(random.randrange(1, 10000)) + \
                "." + str(random.randrange(1000, 10000)) + ".png"
            lista.append([random.randrange(1, values.FLIGHT_LEN),
                          random.randrange(1, values.OBJECTTYPE_LEN), link])

        sql_file_utils.addToFile(cursor,
                                 "object", ["IdFlight", "IdObjectType", "PathToPhoto"], lista)
