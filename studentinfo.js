class Student{
    #studentId = 0;
    #studentName = "";
    #studentAddress= "";
    #totalCGPA = 0.0;
    #totalCredits = 0;

    constructor(id, name, address){
        this.#studentId = id;
        this.#studentName = name;
        this.#studentAddress = address;
    }

    getStudentId(){
        return this.#studentId;
    }

    getStudentName(){
        return this.#studentName;
    }

    getStudentAddress(){
        return this.#studentAddress;
    }

    getCgpa(){
        var cgpa =  this.#totalCGPA / this.#totalCredits;
        if(this.#totalCredits == 0.0){
            return 0.0;
        }
        return cgpa;
    }

    setStudentAddress(address){
        this.#studentAddress = address;
    }

    getTotalCredits(){
        return this.#totalCredits
    }

    addGrade(grade, credits){
        var numericGrade = 0.0;
        switch (grade) {
            case "A+": numericGrade = 4.00; break;
            case "A" : numericGrade = 3.75; break;
            case "A-": numericGrade = 3.50; break;
            case "B+": numericGrade = 3.25; break;
            case "B" : numericGrade = 3.00; break;
            case "B-": numericGrade = 2.75; break;
            case "C+": numericGrade = 2.50; break;
            case "C" : numericGrade = 2.25; break;
            case "D" : numericGrade = 2.00; break;
            case "F" : numericGrade = 0.00; break;
        }
        this.#totalCredits += credits;
        this.#totalCGPA += (numericGrade * credits);
    }

    toString() {
        return this.#studentId + " " + this.#studentName + " " + this.#studentAddress + " " + this.getCgpa();
    }
}

s = new Student(100, 'Manik Mia', "Banani");
s.addGrade("A+", 3.00);
s.addGrade("A", 1.00);
s.addGrade("B+", 3.00);
s.addGrade("B", 3.00);
s.setStudentAddress("Nikunja");
console.log(s+" ");
// console.log(s.getStudentId(), s.getStudentName(), s.getCgpa(), s.getStudentAddress(), s.getTotalCredits());
// For 72 line we use toString
