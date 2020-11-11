from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.sql_file_utils import addToFile
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
        self.__drone = random.randint(1, DRONE_LEN)
        length = random.randint(10, 50)
        self.__description = rand_string(length)

    @staticmethod
    def generate_all(cursor):
        values = []

        instance = Flaw()
        for i in range(FLAW_LEN):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile(cursor, "flaw", ["IdUser", "IdFlight", "IdDrone", "Description"], values)
