from utilitiees import addToFile
import values


class Role():
    @staticmethod
    def generate_all():
        data = open("Role.txt",'r').read().split(',')
        data.pop()

        listOfList = []
        
        for row in data:
            listOfList.append([row])

        values.ROLE_LEN = len(data)
        addToFile.addToFile("role", ["RoleType"], listOfList)