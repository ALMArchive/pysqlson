import numbers


def is_num(val):
    return isinstance(val, numbers.Number)


def is_str(val):
    return isinstance(val, str)


def is_list(val):
    return isinstance(val, list)


def is_dict(val):
    return isinstance(val, dict)


def includes(lst, value):
    if value in lst:
        return True
    else:
        return False
