"""
    A stack is a First-In Last-Out (FILO) queue object (think a stack of books or plates).
    They are useful for things like browser history or other ordering operations like that.

    Python lists are often used as if they were stacks, but they are not strictly stack objects.
    This is because you can dynamically add and remove items anywhere in them, whereas a stack is strictly FILO.

    Here is a class definition for a Stack.
"""


class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

