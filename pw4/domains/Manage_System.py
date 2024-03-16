import math
import numpy as np
import input1
class Manage_system:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        self.GPA = {}

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
            for i,course, in enumerate(self.courses,1):
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
                mark_value = math.floor(float(input(f"Enter mark for {student_selected.name} in {course_selected.name}: ")))
                student_course_key= (student_selected.name,course_selected.name)               
                self.marks[student_course_key]=mark_value
            else:
                print("Invalid course choice!!!")
        else:
            print("Invalid student choice!!!")

    def list_mark(self):
        print(self.marks)
        if not self.marks:
            print("There are no marks to show !!")
        else:
            for i, (student_course_key, mark_value) in enumerate(self.marks.items(), 1):
                student_name, course_name = student_course_key
                print(f"{i}. Name: {student_name}, Course: {course_name}, Mark: {mark_value}")
    
    def add_mark(self, student_course_key, mark_value):
        self.marks[student_course_key] = mark_value
    
    def calculate_GPA(self):
        student_choice = input1.input_student_for_gpa(self.students)
        if 1 <= student_choice <= len(self.students):
            student_selected = self.students[student_choice - 1]
            marks_sum = 0
            total_credits = 0
            for course in self.courses:
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