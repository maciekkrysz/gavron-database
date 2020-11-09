from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string, rand_date_in_range
from utilities.sql_file_utils import addToFile
from values import *

import random

class Flight(SqlDataClass):
    __drone = ""
    __flight_schedule = ""
    __start_date = ""

    def generate_sql(self) -> str:
        return [self.__drone, self.__flight_schedule, self.__start_date]

    def generate_instance(self):
        self.__drone = random.randint(1, DRONE_LEN)
        self.__flight_schedule = random.randint(1, FLIGHTSCHEDULE_LEN)
        self.__start_date = rand_date_in_range("01-01-2020", "09-11-2020")

    @staticmethod
    def generate_all():
        values = []

        instance = Flight()
        for i in range(USER_LEN):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile("flight", ["Drone", "Flight schedule", "Start date"], values)
