"""
    There are three types of edits that can be performed on strings: insert a char, remove a char, or replace a char.
    Given two strings, write a function to check if they are one edit (or zero edits) away.
"""

def find_replace(s1, s2):
    i = 0
    j = 0
    diff_found = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if diff_found:
                return False
            diff_found = True
        i += 1
        j += 1
    return True


def find_ins_rem(s1, s2):
    i = 0
    j = 0
    diff_found = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if diff_found:
                return False
            diff_found = True
            j += 1
        i += 1
        j += 1
    return True


def one_way(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    elif abs(len(s1) - len(s2)) == 1:
        return find_ins_rem(min(s1, s2, key=len), max(s1, s2, key=len))
    else:
        return find_replace(s1, s2)


assert one_way('pale', 'ple') is True
assert one_way('pales', 'pale') is True
assert one_way('pale', 'bale') is True
assert one_way('pale', 'bake') is False
assert one_way('pale', 'bakes') is False

"""
    Could refactor all functions into one like so.
"""


def one_way_refact(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    i = 0
    j = 0
    diff_found = False
    longer = s1 if len(s1) > len(s2) else s2
    shorter = s2 if len(s1) > len(s2) else s1
    while i < len(longer) and j < len(shorter):
        if shorter[i] != longer[j]:
            if diff_found:
                return False
            diff_found = True
            if len(longer) != len(shorter):
                j += 1
        i += 1
        j += 1
    return True


assert one_way_refact('pale', 'ple') is True
assert one_way_refact('pales', 'pale') is True
assert one_way_refact('pale', 'bale') is True
assert one_way_refact('pale', 'bake') is False
assert one_way_refact('pale', 'bakes') is False
assert one_way_refact('paleor', 'pale') is False
assert one_way_refact('bales', 'balez') is True
