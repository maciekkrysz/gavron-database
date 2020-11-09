from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.addToFile import addToFile
from values import *
import random



class Flaw(SqlDataClass):

    __user = ""
    __flight = ""
    __drone = ""
    __description = ""

    def generate_sql(self) -> str:
        return [self.__user, self.__flight, self.__drone, self.__description]

    def generate_instance(self):
        self.__user = random.randint(1, USER_LEN)
        self.__flight = random.randint(1, FLIGHT_LEN)
        self.__drone = random.randint(1, ROLE_LEN)
        self.__description = random.randint(1, ACCOUNT_LEN)

    @staticmethod
    def generate_all():
        values = []

        instance = Flaw()
        for i in range(FLAW_LEN):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile("flaw", ["User", "Flight", "Drone", "Description"], values)
