from data_classes.sql_abstract_class import SqlDataClass
from utilities.generator_utils import rand_string
from utilities.sql_file_utils import addToFile
from utilities.db_conn_utilities import get_all_index
from values import *

import random


class User(SqlDataClass):

    __account = 0
    __role = 0
    roles_indexes = None
    
    def generate_sql(self) -> str:
        return [self.__account, self.__role]

    def generate_instance(self, roles_indexes):
        random_role = random.randint(0, len(roles_indexes) - 1)
        self.__role = roles_indexes[random_role]

    @staticmethod
    def generate_all(cursor):
        values = []
        roles_indexes = get_all_index(cursor, 'role')
        account_indexes = get_all_index(cursor, 'account')

        accounts_added = sorted(account_indexes)[-ACCOUNT_LEN::]
        
        instance = User()
        for account in accounts_added:
            instance.__account = account

            instance.generate_instance(roles_indexes)
            sql_string = instance.generate_sql()
            values.append(sql_string)

        addToFile(cursor, "user", ["IdAccount", "IdRole"], values)
