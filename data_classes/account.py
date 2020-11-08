from data_classes.sql_abstract_class import SqlDataClass


class Account(SqlDataClass):
    def generate_sql(self):
        pass

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all():
        pass
