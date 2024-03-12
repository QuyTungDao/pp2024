class student:
    def __init__(self,student_id,name,DoB):
        self.student_id = student_id
        self.name = name
        self.DoB = DoB
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, DOB: {self.DoB}"

class course:
    def __init__(self,course_id,name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"Name: {self.name}, ID: {self.course_id}"

class Manage_system:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def add_student(self,student):
        self.students.append(student)
    
    def list_student(self):
        if not self.students:
            print("There are no students to show !!")
        else:
            for i,student in enumerate(self.students,1):
                print(f"{i},{student}")
        
    
    def add_course(self,course):
        self.courses.append(course)
    
    def list_courses(self):
        if not self.courses:
            print("There are no course to show !!")
        else:
            for i,course in enumerate(self.courses,1):
                print(f"{i}: {course}")
    
    def input_mark(self):
        if not self.students or not self.courses:
            print("There are no student or course in the list !!")
        else:
            self.list_student()
            student_choice=int(input("Choose a student to enter mark: "))
        if 1<= student_choice<= len(self.students):
            student_selected= self.students[student_choice-1]

            self.list_courses()
            course_choice = int(input("Choose a course: "))
        
            if 1<= course_choice <= len(self.courses):
                course_selected = self.courses[course_choice-1]
                mark_value = float(input(f"Enter mark for {student_selected.name} in {course_selected.name}: "))

                student_course_key= (student_selected.name,course_selected.name)               
                self.marks[student_course_key]=mark_value
            else:
                print("Invalid course choice!!!")
        else:
            print("Invalid student choice!!!")

    def list_mark(self):
        if not self.marks:
            print("There are no mark to show !!")
        else:
            for i, ((student_name,course_name),mark_value) in enumerate (self.marks.items(),1):
                print(f"{i}. Name: {student_name}, Course: {course_name}, Mark: {mark_value}")


mark = Manage_system()

while True:
    print("""
    ==============================================================
    0. Exit
    1. Input student's information
    2. Student's list
    3. Input course's information
    4. course's list
    5. Input mark
    6. Mark's list
    ==============================================================
    """)
    option = int(input("Your choice: "))
    if option == 0:
        break
    elif option == 1:
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            name = input("Enter student's name: ")
            id = input("Enter student's ID: ")
            DoB = input("Enter student's DoB (dd/mm/yy): ")
            stu = student(id,name,DoB)
            mark.add_student(stu)
    elif option == 2:
        mark.list_student()
    elif option == 3:
        num_courses = int(input("Enter number of course: "))
        for i in range(num_courses):
            id = input("Enter course's ID: ")
            name = input("Enter course's name: ")
            cour= course(id,name)
            mark.add_course(cour)
    elif option == 4:
        mark.list_courses()
    elif option == 5:
        mark.input_mark()
    elif option == 6:
        mark.list_mark()
    

        