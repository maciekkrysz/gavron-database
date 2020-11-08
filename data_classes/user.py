from data_classes.sql_abstract_class import SqlDataClass
from utilitiees.pswd_generator import rand_string
from utilitiees.addToFile import addToFile
from values import *

import random


class User(SqlDataClass):

    __account = ""
    __role = ""

    def generate_sql(self) -> str:
        return [self.__account, self.__role]

    def generate_instance(self):
        self.__role = random.randint(0, ROLE_LEN - 1)
        self.__account = random.randint(0, ACCOUNT_LEN - 1)

    @staticmethod
    def generate_all():
        values = []

        instance = User()
        for i in range(USER_LEN):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile("user", ["Account", "Role"], values)
