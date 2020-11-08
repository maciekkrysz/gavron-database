from data_classes.sql_abstract_class import SqlDataClass


class Flaw(SqlDataClass):
    def generate_sql(self):
        pass

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all():
        pass
