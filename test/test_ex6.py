import pytest
from source.Student import Student
from datetime import datetime

@pytest.fixture(scope="module")
def dummy_student():
    print("\n number of creation")
    return Student("gunish",datetime(2000,1,1),"gnmn")

def test_student_age(dummy_student):
    assert dummy_student.get_age() == 7995

def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5

def test_student_check_credits(dummy_student):
    assert dummy_student.get_credits() == 5 # because single object is being used