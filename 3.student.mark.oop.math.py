import math
import numpy as np
class student:
    def __init__(self,student_id,name,DoB):
        self.student_id = student_id
        self.name = name
        self.DoB = DoB
        self.students = []

    def add_student(self,student):
        self.students.append(student)
    
    def list_student(self):
        if not self.students:
            print("There are no students to show !!")
        else:
            for i,student in enumerate(self.students,1):
                print(f"{i},{student}")

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, DOB: {self.DoB}"

class course:
    def __init__(self,course_id,name,credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit
        self.courses = []

    def add_course(self,course):
        self.courses.append(course)
    
    def list_courses(self):
        if not self.courses:
            print("There are no course to show !!")
        else:
            for i,course in enumerate(self.courses,1):
                print(f"{i}: {course}")

    def __str__(self):
        return f"Name: {self.name}, ID: {self.course_id}, Credit: {self.credit}"

class Manage_system:
    def __init__(self):
        self.marks = {}
        self.GPA = {}
    
    def input_mark(self):
        if not students.students or not courses.courses:
            print("There are no student or course in the list !!")
        else:
            students.list_student()
            student_choice=int(input("Choose a student to enter mark: "))
            if 1<= student_choice<= len(students.students):
                student_selected= students.students[student_choice-1]

                courses.list_courses()
                course_choice = int(input("Choose a course: "))
            
                if 1<= course_choice <= len(courses.courses):
                    course_selected = courses.courses[course_choice-1]
                    mark_value = math.floor(float(input(f"Enter mark for {student_selected.name} in {course_selected.name}: ")))
                    student_course_key= (student_selected.name,course_selected.name)               
                    self.marks[student_course_key]= mark_value
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
    
    def calculate_GPA(self):
        students.list_student()
        student_choice = int(input("Select the student that you want to calculate GPA (1-...): "))
        if 1 <= student_choice <= len(students.students):
            student_selected = students.students[student_choice - 1]
            marks_sum = 0
            total_credits = 0
            for course in courses.courses:
                student_course_key = (student_selected.name, course.name)
                if student_course_key in self.marks:
                    mark = self.marks[student_course_key]
                    credit = int(course.credit)
                    marks_sum += mark * credit
                    total_credits += credit

            if total_credits == 0:
                print(f"No marks found for {student_selected.name}")
            else:
                GPA = marks_sum / total_credits
                print(f"GPA for {student_selected.name}: {GPA:.2f}")
                self.GPA[student_selected.name] = GPA
        else:
            print("Invalid student choice!!!")
        
    def sort_GPA(self):
        if not self.GPA:
            print("No GPA data available to sort.")
        else:
            names = np.array(list(self.GPA.keys()))
            GPA_values = np.array(list(self.GPA.values()))
            sorted_indices = np.argsort(-GPA_values)
            sorted_names = names[sorted_indices]
            sorted_GPA = GPA_values[sorted_indices]
            print("Sorted GPA (highest to lowest):")
            for i, (name, GPA) in enumerate(zip(sorted_names, sorted_GPA), 1):
                print(f"""{i}. {name}: {GPA:.2f}""")


students = student(None, None, None) 
courses = course(None, None, None)
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
    7. Calculate GPA
    8. Sorting GPA
    ==============================================================
    """)
    option = int(input("Your choice: "))
    if option == 0:
        print("\n Good Bye !")
        break
    elif option == 1:
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            name = input("Enter student's name: ")
            id = input("Enter student's ID: ")
            DoB = input("Enter student's DoB (dd/mm/yy): ")
            stu = student(id,name,DoB)
            students.add_student(stu)
    elif option == 2:
        students.list_student()
    elif option == 3:
        num_courses = int(input("Enter number of course: "))
        for i in range(num_courses):
            id = input("Enter course's ID: ")
            name = input("Enter course's name: ")
            credit = input("Enter course's credit: ")
            cour= course(id,name,credit)
            courses.add_course(cour)
    elif option == 4:
        courses.list_courses()
    elif option == 5:
        mark.input_mark()
    elif option == 6:
        mark.list_mark()
    elif option ==7:
        mark.calculate_GPA()
    elif option == 8:
        mark.sort_GPA()
    else:
        print("""
              Please input a valid option !!
              ==============================""")