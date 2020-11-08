from data_classes.sql_abstract_class import SqlDataClass


class Flaw(SqlDataClass):

    __id = 0


    def get_id(self):
        return self.__id

    def generate_sql(self):
        pass

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all():
        pass
