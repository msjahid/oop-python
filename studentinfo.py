class Student:
    
    __totalCGPA = 0.0
    __totalCredits = 0

    def __init__(self, id, name, address):
        self.__studentId = id
        self.__studentName = name 
        self.__studentAddress = address 

    def getStudentId(self):
        return self.__studentId

    def getStudentName(self):
        return self.__studentName

    def getStudentAddress(self):
        return self.__studentAddress

    def getCgpa(self):
        cgpa =  self.__totalCGPA / self.__totalCredits
        if(self.__totalCredits == 0.0):
            return 0.0
        return cgpa

    def setStudentAddress(self, address):
        self.__studentAddress = address

    def getTotalCredits(self):
        return self.__totalCredits

    def addGrade(self, grade, credits):
        numericGrade = 0.0
        if (grade == "A+"):
            numericGrade = 4.0
        elif (grade == "A"):
            numericGrade = 3.75
        elif (grade == "A-"):
            numericGrade = 3.50
        elif (grade == "B+"):
            numericGrade = 3.25
        elif (grade == "B"):
            numericGrade = 3.00
        elif (grade == "B-"):
            numericGrade = 2.75
        elif (grade == "C+"):
            numericGrade = 2.50
        elif (grade == "C"):
            numericGrade = 2.25
        elif (grade == "D"):
            numericGrade = 2.00
        elif (grade == "F"):
            numericGrade = 0.00
        else:
            return None
        self.__totalCredits += credits
        self.__totalCGPA += (numericGrade * credits)

    #In java this one called toString
    def __str__(self):
     return str(self.__studentId) + " " +self.__studentName + " " + self.__studentAddress + " " +str(self.getCgpa()) + " " + str(self.getTotalCredits())



s = Student(100, 'Manik Mia', "Banani")
s.addGrade("A+", 3.00)
s.addGrade("A", 1.00)
s.addGrade("B+", 3.00)
s.addGrade("B", 3.00)
s.setStudentAddress("Nikunja")
print(s)
# print(s.getStudentName(), s.getCgpa())
# For 72 number line we use returning a string representation __str__
# print(s.__str__())

