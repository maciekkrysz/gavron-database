from pony.orm import *
import pymysql.cursors

set_sql_debug(True)

# connect to the local database
conn = pymysql.connect(host='localhost',
                       user='root',
                       password="",
                       db='gavron',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()
# some other statements  with the help of cursor
retrive = "SELECT COUNT(*) FROM flight; "
cursor.execute(retrive)
row = cursor.fetchall()[0]

print(row)
thisdict = list(row.values())[0]
print(thisdict) # print count of flight rows
#    print(row['Count(*)'])


conn.close()
