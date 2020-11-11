from data_classes.sql_abstract_class import SqlDataClass
from utilities.sql_file_utils import addToFile
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
        logslen = random.randint(LOG_LEN * 0.80, LOG_LEN)
        seconds = 0

        for i in range(logslen):
            seconds += random.randint(5, 15)
            values_logs.append([j + 1, seconds, getRandDouble(Wroclaw_Longitude),
                                getRandDouble(Wroclaw_Latitude), round(random.random() * 40, 2)])


        addToFile(cursor, "log", ["IdFlight", "SecondsSinceStart",
                                  "Longitude", "Latitude", "Altitude"], values_logs)

def getRandDouble(coord):
    return round(random.uniform(coord-1, coord+1), 5)
