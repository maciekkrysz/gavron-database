import values


def get_count_table(cursor, table_name) -> int:

    retrive = f"SELECT COUNT(*) FROM {table_name};"
    cursor.execute(retrive)
    return cursor.fetchall()[0][0]


def get_all_index(cursor, table_name, index_column_name = 'Id') -> list:

    retrive = f"SELECT {index_column_name} FROM {table_name};"
    cursor.execute(retrive)
    row = [item[0] for item in cursor.fetchall()]
    return row


def drop_database(cursor):
    retrive = "DROP DATABASE gavron;"
    cursor.execute(retrive)

    retrive = "CREATE DATABASE gavron;"
    cursor.execute(retrive)
