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
        if(self.__totalCredits == 0.0 and self.__totalCGPA == 0):
            return 0
        # try:
        #     cgpa =  self.__totalCGPA / self.__totalCredits
        # except ZeroDivisionError:
        #     return 0

        #     if(self.__totalCredits == 0.0):
        #         return 0.0
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


studentList = []
studentList.append(Student(100, "Abul", "Uttara"))
studentList.append(Student(101, "Babul", "Kalabagan"))
studentList.append(Student(102, "Kabul", "Malibagh"))
studentList.append(Student(103, "Abul", "Mirpur"))
studentList.append(Student(104, "Putul", "Nakhalpara"))

studentList[0].addGrade("A+", 1)
studentList[4].addGrade("A", 3)
studentList[3].addGrade("B+", 3)
studentList[3].addGrade("C+", 3)
studentList[2].addGrade("C+", 3)
studentList[1].addGrade("B+", 3)
studentList[1].addGrade("A+", 3)


# print(studentList.sort()) output is None because list object is not sortable in this way
# print(sorted(studentList)) In this way is not working because only one attribute compareable

#---Now we will sort by students cgpa
student_sorted_cgpa = [student.getCgpa() for student in studentList]  
print(sorted(student_sorted_cgpa))
#Python reverse= False is default Ascending order small to large
# print(sorted(student_sorted_cgpa, reverse=True)) here Descending order large to small

