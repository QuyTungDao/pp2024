import math
from domains import course_class, student_class
def input_student():
    num_students = int(input("Enter number of students: "))
    students = []
    for i in range(num_students):
        name = input("Enter student's name: ")
        id = input("Enter student's ID: ")
        DoB = input("Enter student's DoB (dd/mm/yy): ")
        stu = student_class.student(id, name, DoB)
        students.append(stu)
    return students

def input_course():
    num_courses = int(input("Enter number of courses: "))
    courses = []
    for i in range(num_courses):
        id = input("Enter course's ID: ")
        name = input("Enter course's name: ")
        credit = input("Enter course's credit: ")
        cour = course_class.course(id, name, credit)
        courses.append(cour)
    return courses

def input_mark(students, courses):
    if not students or not courses:
        print("There are no student or course in the list !!")
    else:
        print("Students:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
        student_choice = int(input("Choose a student to enter mark: "))
        if 1 <= student_choice <= len(students):
            student_selected = students[student_choice - 1]

            print("Courses:")
            for i, course in enumerate(courses, 1):
                print(f"{i}. {course}")
            course_choice = int(input("Choose a course: "))

            if 1 <= course_choice <= len(courses):
                course_selected = courses[course_choice - 1]
                mark_value = math.floor(float(input(f"Enter mark for {student_selected.name} in {course_selected.name}: ")))
                student_course_key = (student_selected.name, course_selected.name)
                return student_course_key, mark_value
            else:
                print("Invalid course choice!!!")
        else:
            print("Invalid student choice!!!")

def input_student_for_gpa(students):
    if not students:
        print("There are no students in the list !!")
    else:
        print("Students:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
        student_choice = int(input("Select the student that you want to calculate GPA: "))
        return student_choice