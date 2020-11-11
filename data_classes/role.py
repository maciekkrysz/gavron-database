from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.sql_file_utils import addToFile
from values import *


class Role():
    @staticmethod
    def generate_all(cursor):
        data = open("Role.txt", 'r').read().split(',')
        data.pop()

        listOfList = []

        for row in data:
            listOfList.append([row])

        ROLE_LEN = len(data)
        addToFile(cursor, "role", ["NameRole"], listOfList, ignore=True)
