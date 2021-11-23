
from source.PNStudent import is_eligible_for_degree
from datetime import datetime
import pytest

def test_student_get_credits(dummy_pnstudent):
    assert dummy_pnstudent.get_age() == 7995



def test_student_is_eligible_for_degree(make_dummy_pnstudent):
    assert is_eligible_for_degree(make_dummy_pnstudent("sam",datetime(20, 1, 1))) is True


@pytest.mark.parametrize("ages,expected",[(datetime(2025, 1, 1),False),(datetime(2020, 1, 1),True)])
def test_student_is_eligible_for_degree(make_dummy_pnstudent,ages,expected):
    assert is_eligible_for_degree(make_dummy_pnstudent("sam",ages)) is expected
