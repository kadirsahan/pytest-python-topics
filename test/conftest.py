from datetime import datetime

import pytest

from source.NStudent import NStudent
from source.PNStudent import PNStudent


@pytest.fixture
def dummy_nstudent():
    return NStudent("nikhil", datetime(2000, 1, 1), "coe", 20)

# paranteric fixture
@pytest.fixture(params=[19,20], ids=["elgilible", "noneligible"])
def dummy_pnstudent(request):
    return PNStudent("nikhil", datetime(2000, 1, 1), "coe",request.param)


# fixture
@pytest.fixture
def make_dummy_nstudent():
    def _make_dummy_student(name, credits):
        return NStudent(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student

@pytest.fixture
def make_dummy_pnstudent():
    def _make_dummy_pnstudent(name, age):
        return PNStudent(name, age, "coe", 20)

    return _make_dummy_pnstudent