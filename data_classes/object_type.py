from sql_abstract_class import SqlDataClass


class ObjectType(SqlDataClass):
    def generate_sql(self):
        pass

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all():
        pass

def read_from_file():
    dane = open("../pointtype.txt",'r').read().split(',')
    print(dane)

read_from_file()