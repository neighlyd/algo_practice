"""
https://bradfieldcs.com/algos/stacks/converting-number-bases/

"The Divide by 2 algorithm assumes that we start with an integer greater than 0. A simple iteration then continually
divides the decimal number by 2 and keeps track of the remainder. The first division by 2 gives information as to
whether the value is even or odd. An even value will have a remainder of 0. It will have the digit 0 in the ones place.
An odd value will have a remainder of 1 and will have the digit 1 in the ones place. We think about building our binary
number as a sequence of digits; the first remainder we compute will actually be the last digit in the sequence. As shown
 below, we again see the reversal property that signals that a stack is likely to be the appropriate data structure for
 solving the problem."

"""
from algorithm_course.stacks import Stack


def convert_to_binary(decimal_num):

    remainder_stack = Stack()

    while decimal_num > 0:
        remainder = decimal_num % 2
        remainder_stack.push(remainder)
        decimal_num = decimal_num // 2

    binary_digits = []
    while not remainder_stack.is_empty():
        binary_digits.append(str(remainder_stack.pop()))

    return ''.join(binary_digits)


def convert_to_binary_shorter(dec_num):
    stack = []

    while dec_num > 0:
        stack.append(dec_num%2)
        dec_num = dec_num // 2

    return ''.join(str(x) for x in stack[::-1])


DIGITS = '0123456789abcdef'

def convert_to_base(dec_num, base):
    stack = []

    while dec_num > 0:
        stack.append(dec_num%base)
        dec_num = dec_num // base

    new_digits = []
    while stack:
        # uses the remainder as the index from DIGITS to implement the appropriate return digit.
        new_digits.append(DIGITS[stack.pop()])
    return ''.join(new_digits)


print(convert_to_binary(42))
print(convert_to_base(25, 2))  # => '11001'
print(convert_to_base(25, 16))  # => '19'
print(convert_to_base(10, 16))  # => 'a'
