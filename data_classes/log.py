from data_classes.sql_abstract_class import SqlDataClass
from utilities.sql_file_utils import addToFile
from utilities.db_conn_utilities import get_all_index
import random
from values import *


class Log(SqlDataClass):
    def generate_sql(self):
        pass

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all(cursor):
        values_logs = []

        flight_indexes = get_all_index(cursor, 'flight')
        flight_added = sorted(flight_indexes)[-FLIGHT_LEN::]


        for id_flight in flight_added:
            seconds = 0
            logslen = random.randint(LOG_LEN * 0.80, LOG_LEN)
            for log in range(logslen):
                seconds += random.randint(5, 15)
                longitude = getRandDouble(Wroclaw_Longitude)
                latitude = getRandDouble(Wroclaw_Latitude)
                altitude = round(random.random() * 40, 2)

                values_logs.append(
                    [id_flight, seconds, longitude, latitude, altitude])

        addToFile(cursor, "log", ["IdFlight", "SecondsSinceStart",
                                  "Longitude", "Latitude", "Altitude"], values_logs)


def getRandDouble(coord):
    return round(random.uniform(coord-0.3, coord+0.3), 5)
