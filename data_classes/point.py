from utilities.db_conn_utilities import get_all_index
import values
import random

from utilities import sql_file_utils


class Point():

    @staticmethod
    def generate_all(cursor):
        lista = []
        for i in range(values.POINT_LEN):
            point_type_indexes = get_all_index(cursor, 'pointtype')
            random_point_type = random.randint(0, len(point_type_indexes) - 1)

            idPoint = point_type_indexes[random_point_type]

            longitude = round(random.uniform(
                values.Wroclaw_Longitude-1, values.Wroclaw_Longitude+1), 5)

            latitude = round(random.uniform(
                values.Wroclaw_Latitude-1, values.Wroclaw_Latitude+1), 5)

            lista.append([idPoint, longitude, latitude])

        sql_file_utils.addToFile(cursor,
                                 "point", ["IdPointType", "Longitude", "Latitude"], lista)
