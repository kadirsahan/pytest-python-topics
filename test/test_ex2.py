from source.sample2 import validate_number
import pytest
def test_nmbr():
    validate_number(1)

def test_validate_invalid_number():
    with pytest.raises(ValueError) as exc_info:
        validate_number(-11)
    assert str(exc_info.value) == "number cannot be less than 0"