"""
Given a string containing only the characters x and y, find whether there are the same number of xs and ys.

balanced("xxxyyy") => true
balanced("yyyxxx") => true
balanced("xxxyyyy") => false
balanced("yyxyxxyxxyyyyxxxyxyx") => true
balanced("xyxxxxyyyxyxxyxxyy") => false
balanced("") => true
balanced("x") => false
Optional bonus
Given a string containing only lowercase letters, find whether every letter that appears in the string appears the same number of times. Don't forget to handle the empty string ("") correctly!

balanced_bonus("xxxyyyzzz") => true
balanced_bonus("abccbaabccba") => true
balanced_bonus("xxxyyyzzzz") => false
balanced_bonus("abcdefghijklmnopqrstuvwxyz") => true
balanced_bonus("pqq") => false
balanced_bonus("fdedfdeffeddefeeeefddf") => false
balanced_bonus("www") => true
balanced_bonus("x") => true
balanced_bonus("") => true
Note that balanced_bonus behaves differently than balanced for a few inputs, e.g. "x".
"""


def balanced(s):
    if len(s) == 0:
        return True
    elif len(s) % 2 == 1:
        return False
    r = 0
    for c in s:
        if c == 'x':
            r += 1
        elif c == 'y':
            r -= 1
    return r == 0


assert balanced("xxxyyy") is True
assert balanced("yyyxxx") is True
assert balanced("xxxyyyy") is False
assert balanced("yyxyxxyxxyyyyxxxyxyx") is True
assert balanced("xyxxxxyyyxyxxyxxyy") is False
assert balanced("") is True
assert balanced("x") is False


def balanced_bonus(s):
    if len(s) == 0 or len(s) == 1:
        return True
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    # Throw all the values from the dictionary into a set, so any repeats are tossed.
    # If that set is longer than 1, then I know there are letters that appear in different frequencies.
    # However, if the length of set() is 1, then we're all good and return True.
    return len(set(i for i in d.values())) == 1

assert balanced_bonus("xxxyyyzzz") is True
assert balanced_bonus("abccbaabccba") is True
assert balanced_bonus("xxxyyyzzzz") is False
assert balanced_bonus("abcdefghijklmnopqrstuvwxyz") is True
assert balanced_bonus("pqq") is False
assert balanced_bonus("fdedfdeffeddefeeeefddf") is False
assert balanced_bonus("www") is True
assert balanced_bonus("x") is True
assert balanced_bonus("") is True
