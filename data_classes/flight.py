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
        values_logs = []

        instance = Flight()
        for i in range(USER_LEN):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

            logslen = random.randint(100, 400)
            seconds = 0
            for j in range(logslen):
                seconds += random.randint(5, 15)
                values_logs.append([i + 1, seconds, getRandDouble(Wroclaw_Longitude),
                                    getRandDouble(Wroclaw_Latitude), round(random.random() * 40, 2)])

        addToFile("flight", ["Drone", "Flight schedule", "Start date"], values)
        addToFile("logs", ["Flight", "Seconds from start",
                           "Coord x", "Coord y", "Coord z"], values_logs)


def getRandDouble(coord):
    return round(random.uniform(coord-1, coord+1), 5)
