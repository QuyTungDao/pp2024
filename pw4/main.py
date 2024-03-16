import input1
import output
from domains import student_class, course_class, Manage_System

def main():
    mark_system = Manage_System.Manage_system()

    while True:
        output.print_menu()
        option = int(input("Your choice: "))
        if option == 0:
            print("\nGood Bye!")
            break
        elif option == 1:
            students = input1.input_student()
            for stu in students:
                mark_system.add_student(stu)
        elif option == 2:
            output.print_students(mark_system.students)
        elif option == 3:
            courses = input1.input_course()
            for cour in courses:
                mark_system.add_course(cour)
        elif option == 4:
            output.print_courses(mark_system.courses)
        elif option == 5:
            student_course_key, mark_value = input1.input_mark(mark_system.students, mark_system.courses)
            if student_course_key and mark_value:
                mark_system.add_mark(student_course_key, mark_value)
        elif option == 6:
            output.print_marks(mark_system.marks)
        elif option == 7:
            gpa = mark_system.calculate_GPA()  
        elif option == 8:
            mark_system.sort_GPA()

if __name__ == "__main__":
    main()