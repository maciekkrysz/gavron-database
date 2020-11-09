from utilities import sql_file_utils
import values

class PointType():
    @staticmethod
    def generate_all():
        data = open("pointtype.txt", 'r').read().split(',')
        data.pop()

        listOfList = []

        for row in data:
            listOfList.append([row])

        values.POINTTYPE_LEN = len(data)
        sql_file_utils.addToFile("pointtype", ["NamePointType"], listOfList)
