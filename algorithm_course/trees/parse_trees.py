import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
LEFT_PAREN = '('
RIGHT_PAREN = ')'


def build_parse_tree(expr):
    tree = {}
    stack = [tree]
    node = tree
    for token in expr:
        if token == LEFT_PAREN:
            # build a new left child node and descend into it for the next value.
            node['left'] = {}
            stack.append(node)
            node = node['left']
        elif token == RIGHT_PAREN:
            # pull us to a parent.
            node = stack.pop()
        elif token in OPERATORS.keys():
            # an operator adds itself as root node, then drops us into the right node.
            node['val'] = token
            node['right'] = {}
            stack.append(node)
            node = node['right']
        else:
            # numbers get added to nodes immediately and then pull us into their parents.
            node['val'] = int(token)
            parent = stack.pop()
            node = parent
    return tree


def evaluate(tree):
    # A recursive method to evaluate a built up algebra tree. Evaluates each node recursively.
    try:
        operate = OPERATORS[tree['val']]
        return operate(evaluate(tree['left']), evaluate(tree['right']))
    except KeyError:
        # no left or right, so we are on a leaf. This is a base case.
        return tree['val']