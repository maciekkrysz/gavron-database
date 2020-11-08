from data_classes.sql_abstract_class import SqlDataClass
from utilitiees.pswd_generator import rand_string
from utilitiees.addToFile import addToFile
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
