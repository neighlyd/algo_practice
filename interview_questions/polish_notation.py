"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /.
Each operand may be an integer or another expression. For example:
https://en.wikipedia.org/wiki/Reverse_Polish_notation

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

import operator


def reverse_polish_notation(arr):
    """
        Doesn't check for valid combinations, but does check for zero-div errors.
    :param arr: An array in Reverse Polish Notation (
    :return: Int result or String telling user about 'Zero-Division' error (could do an except code here, but fuckit)
    """
    num_stack = []
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    def eval_op(l, r, oper):
        return oper(l, r)

    for i in arr:
        if i not in opers:
            num_stack.append(int(i))
        else:
            right, left = num_stack.pop(), num_stack.pop()
            if right == 0 and opers[i] == operator.truediv:
                return "You can't divide by zero, you fuckwit."
            else:
                num_stack.append(eval_op(left, right, opers[i]))
    return num_stack.pop()
