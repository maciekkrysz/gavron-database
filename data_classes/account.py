from data_classes.sql_abstract_class import SqlDataClass
from utilitiees import pswd_generator


class Account(SqlDataClass):

    __id = 0
    __login = ""
    __password = ""

    def get_id(self):
        return self.__id

    def generate_sql(self) -> str:
        return f"('{self.__id}','{self.__login}', '{self.__password}')"

    def generate_instance(self):
        pass

    @staticmethod
    def generate_all():
        number_of_vals = random()
        sql_string = ""

        values = []

        instance = Account()
        for i in range(number_of_vals):
            instance.generate_instance()
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile("account", [], values)

