class course:
    def __init__(self,course_id,name,credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"Name: {self.name}, ID: {self.course_id}, Credit: {self.credit}"