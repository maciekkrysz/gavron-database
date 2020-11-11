from utilities import sql_file_utils
import values

class PointType():
    @staticmethod
    def generate_all(cursor):
        data = open("pointtype.txt", 'r').read().split(',')
        data.pop()

        listOfList = []

        for row in data:
            listOfList.append([row])

        values.POINTTYPE_LEN = len(data)
        s = sql_file_utils.addToFile("pointtype", ["NamePointType"], listOfList)
        return s

