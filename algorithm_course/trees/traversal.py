"""
The three ways to move through a tree are:

PreOrder: examine root, then left, then right, recursively.
InOrder: examine the left, root, then right, recursively.
PostOrder: examine left, right, then root, recursively.

"""



def preorder(node):
    if node:
        print(node['val'])
        preorder(node.get('left'))
        preorder(node.get('right'))


def inorder(node):
    if node:
        inorder(node.get('left'))
        print(node['val'])
        inorder(node.get('right'))


def postorder(node):
    if node:
        postorder(node.get('left'))
        postorder(node.get('right'))
        print(node['val'])


def construct_expression(parse_tree):
    """ Reconstruct expressions made with parse_tree with their parentheses. """
    if parse_tree is None:
        return ''

    left = construct_expression(parse_tree.get('left'))
    right = construct_expression(parse_tree.get('right'))
    val = parse_tree['val']

    if left and right:
        return f'({left}{val}{right})'

    return val