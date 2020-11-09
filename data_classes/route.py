from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.addToFile import addToFile
from values import ROUTE_LEN

import random

class Route(SqlDataClass):

    __description = ""

    def generate_sql(self) -> str:
        return [self.__description]

    def generate_instance(self):
        length = random.randint(10, 50)
        self.__description = rand_string(length)


    @staticmethod
    def generate_all():
        values = []

        instance = Route()
        for _ in range(ROUTE_LEN):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile("route", ["Description"], values)

