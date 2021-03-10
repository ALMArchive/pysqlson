import numbers


def is_num(val):
    return isinstance(val, numbers.Number)


def is_str(val):
    return isinstance(val, str)


def is_list(val):
    return isinstance(val, list)


def includes(lst, value):
    if value in lst:
        return True
    else:
        return False
