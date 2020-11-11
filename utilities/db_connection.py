import pymysql.cursors

conn = pymysql.connect(host='localhost',
                        user='root',
                        password="",
                        db='gavron',
                        charset='utf8',
                        cursorclass=pymysql.cursors.Cursor)
cursor = conn.cursor() 

