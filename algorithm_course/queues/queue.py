"""
    Queues work similar to stacks, except they are First-In First-Out (FIFO). This means that the first item added is
    also the first item that is removed from the queue. It is a well-ordered line. Things like keystrokes are queues.

    Queues have several methods:

    `enqueue(item)`: adds a new item to the rear of the queue. Returns None
    `dequeue()`: remove the front item from the queue. Returns the item or None.
    `is_empty()`: Checks whether queue is empty or not. Returns Boolean.
    `size()`: Returns number of items in queue. Returns Int.

    The problem with the below implementation is that `enqueue()` is an O(n) implementation.

"""

class Queue:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def dequeue(self):
        if not self.is_empty():
            return self._items.pop()
        else:
            return None

    def enqueue(self, item):
        self._items.insert(0, item)
