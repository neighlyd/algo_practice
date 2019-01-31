"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.

For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.
"""


def isomorph_check(s1, s2):

    # Make sure we're dealing with strings here, so we don't throw errors for the later steps.
    if not isinstance(s1, str) or not isinstance(s2, str):
        return False

    # If the strings don't have the same length they can't be isomorphic.
    if len(s1) != len(s2):
        return False

    # create a hash map to correlate letters from s1 to s2.
    memo = {}

    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if c1 not in memo:
            memo[c1] = c2
        elif c1 in memo and memo[c1] != c2:
            return False

    return True
