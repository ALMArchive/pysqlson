import numbers


def is_num(val):
    isinstance(val, numbers.Number)


def is_str(val):
    isinstance(val, str)


def is_list(val):
    isinstance(val, list)


def includes(lst, value):
    if value in lst:
        return True
    else:
        return False
