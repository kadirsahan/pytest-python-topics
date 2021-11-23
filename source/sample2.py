def validate_number(nmbr):
    if nmbr <0:
        raise ValueError("number cannot be less than 0")