"""
    Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to is_substring
    (e.g. s2 = 'waterbottle' is a rotation of s1 = 'erbottlewat')
"""


def is_substring(s1, s2):
    """
        Because s1 would be a rotation of s2, its edges would create the full substring when aligned.
        e.g.:
            s1 + s1 = 'erbottlewaterbottlewat'
            This contains the full substring of s2 = 'bottlewater'
    """
    return s2 in s1 + s1


assert is_substring('erbottlewat', 'waterbottle') is True
assert is_substring('notbottlewut', 'waterbottle') is False
assert is_substring('', 'anything') is False
