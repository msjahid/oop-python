# Poly means multiple and morphism means structure. Giving more than one structure to something is called polymorphism. Polymorphism in programming means using the same function differently or behaving differently.
class ShapeDrawer:

    def draw(self):
        pass

    # There are two types of polymorphism methods used in Python. Method overriding and method overloading.

class TriangleDrawer(ShapeDrawer):
    __rows = 0 

    def __init__(self, rows):
        self.__rows = rows 

    def getrows(self):
        return self.__rows

    #Method overriding
    def draw(self):
        rowsLength = self.__rows
        for i in range(0, rowsLength):
            for j in range(0, i+1):
                print("* ",end="")
            print("\r")

class SquareDrawer(ShapeDrawer):
    __rows = 0 

    def __init__(self, rows):
        self.__rows = rows 

    def getrows(self):
        return self.__rows

    def draw(self):
        rowsLength = self.__rows
        for i in range(0, rowsLength):
            for j in range(0, rowsLength):
                print("* ",end="")
            print("\r")

# traingle = TriangleDrawer(4)
# square = SquareDrawer(4)
# traingle.draw()
# square.draw()
triangleList = []
triangleList.append(TriangleDrawer(4))
triangleList.append(TriangleDrawer(3))
triangleList.append(SquareDrawer(3))

for i in triangleList:
    i.draw()
