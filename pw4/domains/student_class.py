class student:
    def __init__(self,student_id,name,DoB):
        self.student_id = student_id
        self.name = name
        self.DoB = DoB
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, DOB: {self.DoB}"