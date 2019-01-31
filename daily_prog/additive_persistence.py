"""
today's challenge is to calculate the additive persistence of a number, defined as how many loops you have to do summing its digits until you get a single digit number. Take an integer N:

Add its digits
Repeat until the result has 1 digit
The total number of iterations is the additive persistence of N.

Your challenge today is to implement a function that calculates the additive persistence of a number
"""


def additive_persistence(n):
    pers_count = 0
    while n > 9:
        n = sum_digits(n)
        pers_count += 1
    return pers_count


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n = n // 10
    return s


assert additive_persistence(13) == 1
assert additive_persistence(1234) == 2
assert additive_persistence(9876) == 2
assert additive_persistence(199) == 3
assert additive_persistence(19999999999999999999999) == 4
