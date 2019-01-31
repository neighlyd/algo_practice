"""

    The exercise here is to check whether a series of parentheses are 'balanced', that is to say - does each open
    parenthesis correspond to an opposite, closed parenthesis.

    examples of balanced parentheses:

    '(()()()())'

    '(((())))'

    '(()((())()))'

    examples of unbalanced parentheses:

    '((((((())'

    '()))'

    '(()()(() '

    We can do this by using a FILO stack.
"""
from algorithm_course.stacks import Stack


def balanced_parentheses(parens):

    # initiate an empty stack.
    stack = Stack()

    # iterate through the string of parentheses.
    for paren in parens:
        # if it is a left parenthesis, push it onto the stack.
        if paren == '(':
            stack.push(paren)
        # Otherwise, if it is a right paren then pop off a left parenthesis, this moves us back through the queue in
        # reverse order (FILO), matching each closing paren with the next-closest opening paren that has yet to be
        # matched.
        elif paren == ')':
            try:
                stack.pop()
            # If we have a closing paren with no correlating opening paren, then this is unbalanced.
            except IndexError:
                return False
    # If we get to the end and there are opening parens left in the stack, but no closing parens left to iterate
    # through, then the stack is unbalanced. Therefore, check the falsity of the length against 0.
    return stack.size() == 0


# Balanced parentheses
assert balanced_parentheses('(()()()())') is True
assert balanced_parentheses('(((())))') is True
assert balanced_parentheses('(()(((12341234))({}}})))') is True

# Unbalanced parentheses
assert balanced_parentheses('()))') is False
assert balanced_parentheses('(()()(()') is False
assert balanced_parentheses('((((((())     ') is False


# Alternatively, we can write something that matches any symbol with its opposite.

PAIRINGS = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def is_balanced(pairs):
    stack = Stack()

    for s in pairs:
        if s in PAIRINGS:
            stack.push(s)
            # Push opening symbol onto stack and then move onto the next symbol with continue
            continue
        elif s in PAIRINGS.values():
            try:
                expected_opening_symbol = stack.pop()
            except IndexError:
                return False
            if s != PAIRINGS[expected_opening_symbol]:
                return False

    return stack.size() == 0


assert is_balanced('{{([][])}()}') is True
assert is_balanced('{{()]') is False
assert is_balanced('((((((())     ') is False
assert is_balanced('{"A": [1, 2, 3, 4], (2, 3): {1, 2, 3}}') is True
