"""
    Given two strings, check that one is a permutation of the other.
"""


def check_permutations(s1, s2):
    if len(s1) != len(s2):
        return False
    # use collections.defaultdict to reduce need for manual error checking.
    d = dict()
    for c in s1:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    for c in s2:
        if c not in d:
            return False
        else:
            d[c] -= 1
        if d[c] < 0:
            return False

    return True


assert check_permutations('acab', 'baac') is True
assert check_permutations('ccab', 'baac') is False
assert check_permutations('', '') is True
