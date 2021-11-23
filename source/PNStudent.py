from datetime import datetime

class PNStudent:
    def __init__(self,name,dob,branch,credits):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credits

    def get_age(self):
        return (datetime.now()-self.dob).days
    def add_credits(self,value):
        self.credits += value
        

def get_topper(students):
    return max(students, key=lambda student: student.get_credits())

def is_eligible_for_degree(student):
    return student.get_age() >= 20