import values

def get_count_table(cursor, table_name):

    retrive = "SELECT COUNT(*) FROM flight;"
    cursor.execute(retrive)
    #print count of retrive
    return cursor.fetchall()[0][0]
    

def drop_database(cursor):
    retrive = "DROP DATABASE gavron;"
    cursor.execute(retrive)

    retrive = "CREATE DATABASE gavron;"
    cursor.execute(retrive)
