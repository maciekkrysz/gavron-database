from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.sql_file_utils import addToFile
from utilities.db_conn_utilities import get_all_index
from values import ROUTE_LEN, POINT_LEN, POINT_ON_ROUTE

import random


class PointOnRoute(SqlDataClass):

    __id_route = 0
    __id_point = 0
    __order = 0

    def generate_sql(self) -> str:
        return [self.__id_route, self.__id_point, self.__order]

    def generate_instance(self, route, point_indexes, order):
        self.__order = order

    @staticmethod
    def generate_all(cursor):
        values = []

        point_indexes = get_all_index(cursor, 'point')
        route_indexes = get_all_index(cursor, 'route')
        routes_added = sorted(route_indexes)[-ROUTE_LEN::]

        instance = PointOnRoute()

        for route in routes_added:
            route_length = random.randint(0.8 * POINT_ON_ROUTE, POINT_ON_ROUTE)
            instance.__order = 0
            instance.__id_route = route

            for _ in range(route_length):
                random_point = random.randint(0, len(point_indexes) - 1)
                instance.__id_point = point_indexes[random_point]

                sql_string = instance.generate_sql()
                values.append(sql_string)

                instance.__order += 1

        addToFile(cursor, "pointonroute", [
                  "IdRoute", "IdPoint", "Order_"], values)
