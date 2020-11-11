from utilities import sql_file_utils
from utilities.db_conn_utilities import get_all_index
from values import *
import random


class Object():
    @staticmethod
    def generate_all(cursor):
        lista = []

        flight_indexes = get_all_index(cursor, 'flight')
        flight_added = sorted(flight_indexes)[-FLIGHT_LEN::]

        for id_flight in flight_added:
            count_obj = random.randint(0.8 * OBJECT_LEN, OBJECT_LEN)
            for i in range(count_obj):
                link = "/" + str(id_flight).zfill(6) + \
                    "_" + str(i + 1).zfill(5) + ".png"

                obj_type_indexes = get_all_index(cursor, 'objecttype')
                random_obj_type = random.randint(0, len(obj_type_indexes) - 1)
                id_obj = obj_type_indexes[random_obj_type]
                
                lista.append([id_flight, id_obj, link])

        sql_file_utils.addToFile(cursor,
                                 "object", ["IdFlight", "IdObjectType", "PathToPhoto"], lista)
