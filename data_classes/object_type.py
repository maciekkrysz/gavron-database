from sql_abstract_class import SqlDataClass
from 


class ObjectType(SqlDataClass):
    def generate_sql(self):
        pass

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all():
        data = open("../pointtype.txt",'r').read().split(',')
        data.pop()
        generate_sql()

        