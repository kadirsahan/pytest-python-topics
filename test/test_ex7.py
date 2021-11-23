
from source.NStudent import get_topper

def test_student_get_credits(dummy_nstudent):
    assert dummy_nstudent.get_credits() == 20


def test_get_topper(make_dummy_nstudent):
    students = [
        make_dummy_nstudent("ram", 21),
        make_dummy_nstudent("shyam", 19),
        make_dummy_nstudent("ravi", 22)
    ]

    topper = get_topper(students)

    assert topper == students[2]
