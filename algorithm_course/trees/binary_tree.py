class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            # bump current child down one level and put this child in its place. Sorry, my dude.
            child.left = self.left
            self.left = child

    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child


"""
You can alternatively store a tree as a list of lists.

tree = [
    'a',  #root
    [
        'b',  # left subtree
        ['d' [], []],
        ['e' [], []]
    ],
    [
        'c',  # right subtree
        ['f' [], []],
        []
    ]
]

tree[0] will give you the root, while tree[1] gives the left subtree, tree[2] gives the right.

The nice thing with this format is that it will allow extensibility (you aren't limited to a binary left-right setup).
The downside is that it's really hard to decipher and maintain.

Here is an example
"""


def insert_left(root, child_val):
    subtree = root.pop(1)
    if len(subtree) > 1:
        root.insert(1, [child_val, subtree, []])
    else:
        root.insert(1, [child_val, [], []])
    return root


def insert_right(root, child_val):
    # presumes binary tree
    subtree = root.pop(2)
    if len(subtree) > 1:
        root.insert(2, [child_val, subtree, []])
    else:
        root.insert(2, [child_val, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, val):
    root[0] = val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


"""
Due to the difficulty in reading this format, it is suggested to use a hash map instead:

For binary trees:

{
    'val': 'A',
    'left': {
        'val': 'B',
        'left': {'val': 'D'},
        'right': {'val': 'E'}
    },
    'right': {
        'val': 'C',
        'right': {'val': 'F'}
    }
}

For non-binary trees:

{
    'val': 'A',
    'children': [
        {
            'val': 'B',
            'children': [
                {'val': 'D'},
                {'val': 'E'},
            ]
        },
        {
            'val': 'C',
            'children': [
                {'val': 'F'},
                {'val': 'G'},
                {'val': 'H'}
            ]
        }
    ]
} 
"""