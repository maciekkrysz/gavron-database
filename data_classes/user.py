from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.sql_file_utils import addToFile
from values import *

import random


class User(SqlDataClass):

    __account = 0
    __role = 0

    def generate_sql(self) -> str:
        return [self.__account, self.__role]

    def generate_instance(self):
        self.__role = random.randint(1, ROLE_LEN)

    @staticmethod
    def generate_all():
        values = []

        instance = User()
        
        for i in range(1, USER_LEN + 1):
            instance.__account = i

            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile("user", ["IdAccount", "IdRole"], values)
