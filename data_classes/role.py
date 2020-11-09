from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.addToFile import addToFile
from values import *



class Role():
    @staticmethod
    def generate_all():
        data = open("Role.txt", 'r').read().split(',')
        data.pop()

        listOfList = []

        for row in data:
            listOfList.append([row])

        values.ROLE_LEN = len(data)
        addToFile.addToFile("role", ["RoleType"], listOfList)
