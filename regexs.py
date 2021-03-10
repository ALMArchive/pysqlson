import re


def _match(pattern, text):
    return re.match(pattern, text) is not None


def regex_and(text):
    return _match('&&', text)


def regex_or(text):
    return _match('||', text)


def regex_eq(text):
    return _match('=', text)


def regex_neq(text):
    return _match('!=', text)


def regex_lt(text):
    return _match('<', text)


def regex_le(text):
    return _match('<=', text)


def regex_gt(text):
    return _match('>', text)


def regex_ge(text):
    return _match('>=', text)


def regex_in(text):
    return _match('in', text)


def regex_like(text):
    return _match('like', text)


def regex_bt(text):
    return _match('..', text)
