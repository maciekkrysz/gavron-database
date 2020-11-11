from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string, rand_date_in_range
from utilities.sql_file_utils import addToFile
from utilities.db_conn_utilities import get_all_index
from values import *

import random


class Flight(SqlDataClass):
    __drone = ""
    __flight_schedule = ""
    __start_date = ""

    def generate_sql(self) -> str:
        return [self.__drone, self.__flight_schedule, self.__start_date]

    def generate_instance(self, drone_indexes, flight_sched_indexes):
        random_drone = random.randint(0, len(drone_indexes) - 1)
        random_flight_sched = random.randint(0, len(flight_sched_indexes) - 1)

        self.__drone = drone_indexes[random_drone]
        self.__flight_schedule = flight_sched_indexes[random_flight_sched]
        self.__start_date = rand_date_in_range("2020-01-01", "2020-09-11")

    @staticmethod
    def generate_all(cursor):
        values = []

        drone_indexes = get_all_index(cursor, 'drone')
        flight_sched_indexes = get_all_index(cursor, 'flightschedule')

        instance = Flight()
        for i in range(FLIGHT_LEN):
            instance.generate_instance(drone_indexes, flight_sched_indexes)
            sql_string = instance.generate_sql()
            values.append(sql_string)


        addToFile(cursor, "flight", ["IdDrone",
                                     "IdFlightSchedule", "StartDate"], values)
