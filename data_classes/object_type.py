from sql_abstract_class import SqlDataClass


class ObjectType(SqlDataClass):
    def generate_sql(self):
        pass

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all():
        pass

    @staticmethod
    def read_from_file():
        data = open("../pointtype.txt",'r').read().split(',')
        data.pop()
        print(data)

ObjectType.read_from_file()