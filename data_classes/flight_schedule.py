from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string, rand_date_in_range
from utilities.sql_file_utils import addToFile
from values import FLIGHTSCHEDULE_LEN, USER_LEN, ROUTE_LEN

import random
import datetime


class FlightSchedule(SqlDataClass):

    __id_user = 0
    __id_route = 0
    __start_date = ""
    __start_minute = 0
    __interval = 0

    def generate_sql(self) -> str:
        return [self.__id_user, self.__id_route, self.__start_date, self.__start_minute, self.__interval]

    def generate_instance(self):
        self.__id_user = random.randint(1, USER_LEN)

        self.__id_route = random.randint(1, ROUTE_LEN)

        self.__start_date = rand_date_in_range("2019-11-01", "2019-12-31")

        self.__start_minute = random.randint(0, 1440)

        self.__interval = random.randrange(60, 43200, 60)

    @staticmethod
    def generate_all(cursor):
        values = []

        instance = FlightSchedule()
        for _ in range(FLIGHTSCHEDULE_LEN):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile("flightschedule", [
                  "IdUser", "IdRoute", "StartDate", "StartMinute", "Interval_"], values)
