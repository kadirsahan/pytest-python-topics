from source.sample3 import add
import pytest
import sys


@pytest.mark.skip(reason="nop")
def test_add_num():
    assert add(1,2)==3



@pytest.mark.skipif(sys.version_info>(3,9), reason=" use python 3.7")
def test_add_str():
    assert add("a","b")=="ab"



@pytest.mark.xfail(sys.platform != "win32" , reason="dont run on windows")
def test_add_str_xfail():
    assert add([1],[2])==[1,2]
    raise Exception()
