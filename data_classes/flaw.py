from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.sql_file_utils import addToFile
from utilities.db_conn_utilities import get_all_index
from values import *
import random



class Flaw(SqlDataClass):

    __user = ""
    __flight = ""
    __drone = ""
    __description = ""

    def generate_sql(self) -> str:
        return [self.__user, self.__flight, self.__drone, self.__description]

    def generate_instance(self, user_indexes, flight_indexes, drone_indexes):
        random_user = random.randint(0, len(user_indexes) - 1)
        random_flight = random.randint(0, len(flight_indexes) - 1)
        random_drone = random.randint(0, len(drone_indexes) - 1)

        self.__user = user_indexes[random_user]
        self.__flight = flight_indexes[random_flight]
        self.__drone = drone_indexes[random_drone]
        length = random.randint(10, 50)
        self.__description = rand_string(length)

    @staticmethod
    def generate_all(cursor):
        values = []
        user_indexes = get_all_index(cursor, 'user')
        flight_indexes = get_all_index(cursor, 'flightschedule')
        drone_indexes = get_all_index(cursor, 'drone')

        instance = Flaw()
        for i in range(FLAW_LEN):
            instance.generate_instance(user_indexes, flight_indexes, drone_indexes)
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile(cursor, "flaw", ["IdUser", "IdFlight", "IdDrone", "Description"], values, True)
