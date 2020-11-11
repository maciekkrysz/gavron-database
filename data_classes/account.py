from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.sql_file_utils import addToFile
from values import *

import random


class Account(SqlDataClass):

    __login = ""
    __password = ""

    def generate_sql(self) -> str:
        return [self.__login, self.__password]

    def generate_instance(self):
        login_length = random.randint(8, 15)
        self.__login = rand_string(login_length)

        passwd_length = random.randint(10, 20)
        self.__password = rand_string(passwd_length)

    @staticmethod
    def generate_all(cursor):
        values = []

        instance = Account()
        for i in range(ACCOUNT_LEN):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile(cursor, "account", ["Login", "Password"], values)
