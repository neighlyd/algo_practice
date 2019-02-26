"""
    Check to see if all of the characters in a string are unique.
"""


def is_unique(s):
    s_set = set()
    for c in s:
        s_set.add(c)
    return len(s) == len(s_set)


assert is_unique('abcd') is True
assert is_unique('acab') is False
assert is_unique('') is True
assert is_unique('!@sjkJK') is True
