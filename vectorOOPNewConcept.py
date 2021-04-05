class Vector:

    def __init__(self, i=0, j=0, k=0):
        self.__i = i
        self.__j = j 
        self.__k = k

    def add(self, b):
        c = Vector()
        c.i = self.__i + b.__i 
        c.j = self.__j + b.__j 
        c.k = self.__k + b.__k 
        return c

    def dot(self, b):
        result = 0
        result = result + self.__i * b.__i
        result = result + self.__j * b.__j
        result = result + self.__k * b.__k
        return result

    def __str__(self):
        return f"({ c.i}, {c.j }, { c.k })"

a = Vector(4, 2, 1)
b = Vector(1, 3, 1)
c = a.add(b)
d = a.dot(b)
print(c)
print(d)
