from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.sql_file_utils import addToFile
from values import ROUTE_LEN, POINT_LEN

import random


class PointOnRoute(SqlDataClass):

    __id_route = 0
    __id_point = 0
    __order = 0

    
    def generate_sql(self) -> str:
        return [self.__id_route, self.__id_point, self.__order]

    def generate_instance(self):
        self.__id_point = random.randint(1, POINT_LEN)

    @staticmethod
    def generate_all():
        values = []

        instance = PointOnRoute()

        for i in range(1, ROUTE_LEN):
            route_length = random.randint(3, 20)
            instance.__order = 0
            instance.__id_route = i
            for _ in range(1, route_length):
                instance.generate_instance()
                sql_string = instance.generate_sql()
                values.append(sql_string)

                instance.__order = instance.__order + 1
            
            instance.__id_route = instance.__id_route + 1

        addToFile("pointonroute", ["IdRoute", "IdPoint", "Order_"], values)
