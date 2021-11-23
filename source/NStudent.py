from datetime import datetime

class NStudent:
    def __init__(self,name,dob,branch,credits):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credits

    def get_age(self):
        return (datetime.now()-self.dob).days
    def add_credits(self,value):
        self.credits += value
    def get_credits(self):
        return self.credits
        

def get_topper(students):
    return max(students, key=lambda student: student.get_credits())