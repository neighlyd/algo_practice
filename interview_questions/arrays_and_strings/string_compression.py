"""
    Implement a method to perform basic string compression using the counts of repeated characters.
    For example, the string aabcccccaaa would become a2b1c5a3.
    If the 'compressed' string would not become smaller than the original string, your method should return the original string.
    You can assume the string has only uppercase and lowercase letters (a-z).
"""


def compress_string(s):
    if len(s) <= 1:
        return s
    curr_char = s[0]
    count = 1
    res = ''
    for i in range(1, len(s)):
        if len(res) >= len(s):
            return s
        if s[i] == curr_char:
            count += 1
        else:
            res = res + curr_char + str(count)
            curr_char = s[i]
            count = 1
    res += curr_char + str(count)
    return min(s, res, key=len)


assert compress_string('aabcccccaaa') == 'a2b1c5a3'
assert compress_string('abc') == 'abc'
assert compress_string('') == ''
assert compress_string('AjbnjSSAaaAA') == 'AjbnjSSAaaAA'
assert compress_string('AaaaaaaaaaaaaaaaaaaaaaaaaaaaaaA##') == 'A1a29A1#2'
