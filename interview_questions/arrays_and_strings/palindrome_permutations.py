"""
    Given a string, write a function to check if it is a permutation of a palindrome.
    The palindrome does not need to be limited to just dictionary words.
    You can ignore casing and non-letter characters.
"""


def palindrome_permutations(s):
    # use collections.defaultdict to reduce error checking in code.
    d = dict()
    s = s.lower().replace(" ", "")

    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    found_odd = False
    for val in d.values():
        if val % 2 != 0:
            if found_odd:
                return False
            found_odd = True

    return True


assert palindrome_permutations('Tact Coa') is True