def print_menu():
    print("""
    ==============================================================
    0. Exit
    1. Input student's information
    2. Student's list
    3. Input course's information
    4. Course's list
    5. Input mark
    6. Mark's list
    7. Calculate GPA
    8. Sorting GPA
    ==============================================================
    """)

def print_students(students):
    if not students:
        print("There are no students to show !!")
    else:
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")

def print_courses(courses):
    if not courses:
        print("There are no courses to show !!")
    else:
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course}")

def print_marks(marks):
    if not marks:
        print("There are no marks to show !!")
    else:
        for i, ((student_name, course_name), mark_value) in enumerate(marks.items(), 1):
            print(f"{i}. Name: {student_name}, Course: {course_name}, Mark: {mark_value}")

def print_gpa(student_name, gpa):
    print(f"GPA for {student_name}: {gpa:.2f}")

def print_sorted_gpa(sorted_gpa):
    if not sorted_gpa:
        print("No GPA data available to sort.")
    else:
        print("Sorted GPA (highest to lowest):")
        for i, (name, gpa) in enumerate(sorted_gpa, 1):
            print(f"{i}. {name}: {gpa:.2f}")