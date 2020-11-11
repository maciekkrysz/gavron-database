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
retrive = "Select * from flight"
cursor.execute(retrive)
rows = cursor.fetchall()
for row in rows:
   print(row)


conn.close()
