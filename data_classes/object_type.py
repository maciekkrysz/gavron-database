from utilities import sql_file_utils
import values


class ObjectType():
    @staticmethod
    def generate_all(cursor):
        data = open("objecttype.txt", 'r').read().split(',')
        data.pop()
        listOfList = []

        for row in data:
            listOfList.append([row])

        values.OBJECTTYPE_LEN = len(data)
        s = sql_file_utils.addToFile("objecttype", ["Name"], listOfList)
        return s
