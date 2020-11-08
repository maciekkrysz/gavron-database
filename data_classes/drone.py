from data_classes.sql_abstract_class import SqlDataClass


class Drone(SqlDataClass):

    __id = ""
    __model_drone = ""

    def get_id(self):
        return self.__id

    def generate_sql(self):
        pass

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all():
        pass

