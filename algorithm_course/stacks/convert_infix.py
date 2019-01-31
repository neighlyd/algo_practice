from string import ascii_letters, digits
from operator import add, sub, mul, truediv

PRECEDENCE = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1
}


def infix_to_postfix(infix):
    oper_stack = []
    tokens = infix.split()
    postfix = []

    for token in tokens:
        if token in ascii_letters or token in digits:
            postfix.append(token)

        elif token == '(':
            oper_stack.append(token)

        elif token == ')':
            top_token = oper_stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = oper_stack.pop()

        else:
            while oper_stack and (PRECEDENCE[oper_stack[-1]] >= PRECEDENCE[token]):
                postfix.append(oper_stack.pop())
            oper_stack.append(token)

    while oper_stack:
        postfix.append(oper_stack.pop())

    print(postfix)
    return ''.join(str(x) for x in postfix)

print(infix_to_postfix('A * B + C * D'))


OPERS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}


def postfix_to_infix(postfix):
    operand_stack = []
    tokens = postfix.split()
    infix = []

    for token in tokens:
        if token in ascii_letters or token in digits:
            operand_stack.append(int(token))
        else:
            if token in OPERS:
                right = operand_stack.pop()
                left = operand_stack.pop()
                operand_stack.append(OPERS[token](left, right))

    return operand_stack.pop()

print(postfix_to_infix('7 8 + 3 2 + /'))
