from data_classes.sql_abstract_class import SqlDataClass
from utilitiees.pswd_generator import rand_string
from utilitiees.addToFile import addToFile

import random

class Account(SqlDataClass):

    __login = ""
    __password = ""

    def get_id(self):
        return self.__id

    def generate_sql(self) -> str:
        return [self.__login, self.__password]

    def generate_instance(self):
        login_length = random.randint(8, 15)
        __login = rand_string(login_length)

        passwd_length = random.randint(10, 20)
        __passwd = rand_string(passwd_length)

    @staticmethod
    def generate_all():
        number_of_vals = random()
        sql_string = ""

        values = []

        instance = Account()
        for i in range(number_of_vals):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile("account", ["Id", "Login", "Password"], values)

