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
        data = open("../pointtype.txt",'r').read().split(',')
        data.pop()
        print(data)

read_from_file()