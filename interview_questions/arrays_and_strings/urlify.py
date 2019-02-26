"""
    Given a string replace spaces internal in the string with %20.
    The string will be padded on the right with enough space to accomodate the extra two characters per space.
    This isn't really necessary in python.
"""

def urlify(s):
    space = '%20'
    s = s.rstrip()
    s = s.replace(' ', space)
    return s


assert urlify('A Test       ') == 'A%20Test'
assert urlify('a long one with lots of spaces') == 'a%20long%20one%20with%20lots%20of%20spaces'


"""
    Could also do regex stuff, but 1) I hate regex, 2) regex is O(n^2) anyway.
"""