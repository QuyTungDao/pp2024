print("===========================================================")

def input_num_of_student():
    return int(input("Enter number of student: "))

def input_student_information():
    student_name=input("Enter student's name: ")
    student_id= input("Enter student's ID : ")
    student_dob=input("Enter student's DOB (DD/MM/YY): ")
    return [student_name,student_id,student_dob]

def list_stu(student):
    print("=======================================================")
    if len(student)==0:
        print("There is no student to show !!!")
    else:
        for i,a in enumerate(student):
            print(f"{i+1}. Name : {a[0]}, ID: {a[1]}, DOB: {a[2]}")

def list_course(course):
    print("=======================================================")
    if len(course)==0:
        print("There is no course to show !!!")
    else:
        for i,a in enumerate(course):
            print(f"{i+1}. Name : {a[0]}, ID: {a[1]}")

def input_num_of_course():
    return int(input("Enter number of course: "))

def input_course_information():
    course_name=input("Enter course's name: ")
    course_id= input("Enter course's ID : ")
    return [course_name,course_id]

def input_student_mark():
    if len(student)==0 or len(course)==0:
        print("There is no student or course in the list !!!")
    else:
        list_stu(student)
        student_choice=int(input("Choose a student to enter mark: "))
        if 1<= student_choice<= len(student):
            student_selected=student[student_choice-1]

            list_course(course)
            course_choice = int(input("Choose a course: "))
        
            if 1<= course_choice <= len(course):
                course_selected = course[course_choice-1]
                mark_value = float(input(f"Enter mark for {student_selected[0]} in {course_selected[0]}: "))

                student_course_key= (student_selected[0],course_selected[0])               
                mark[student_course_key]=mark_value

            else:
                print("Invalid course choice!!!")
        else:
            print("Invalid student choice!!!")

def mark_list(mark):
    if len(mark)==0:
        print("There is no mark to show !!!")
    else:
        print("====================================================")
        for i,(student_name, course_name) in enumerate(mark):
            mark_value=mark[(student_name,course_name)]
            print(f"{i+1}. Name: {student_name}, Course: {course_name}, Mark: {mark_value}")
            

student=[]
course=[]
mark={}
while(True):
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
        num_student=input_num_of_student()
        for i in range(0,num_student):
            student_infor=input_student_information()
            student.append(student_infor)
    elif option ==2:
        list_stu(student)
    elif option ==3:
        num_course=input_num_of_course()
        for i in range(0,num_course):
            course_infor=input_course_information()
            course.append(course_infor)
    elif option ==4:
        list_course(course)
    elif option ==5:
        input_student_mark()
    elif option ==6:
        mark_list(mark)