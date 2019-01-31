"""
This priority queue uses a binary heap, which allows us to enqueue and dequeue items in O(log n).

Although a priority queue looks like a tree when mapped out, we use a flat array to represent it internally.

The two types of priority queues are min_heap and max_heap - min and max can be judged against any value you wish.

The basic operations we will implement for our binary heap are:

BinaryHeap() creates a new, empty, binary heap.
insert(k) adds a new item to the heap.
find_min() returns the item with the minimum key value, leaving item in the heap.
pop() returns the item with the minimum key value, removing the item from the heap.
is_empty() returns true if the heap is empty, false otherwise.
size() returns the number of items in the heap.
build_heap(list) builds a new heap from a list of keys.

Using a list to locate children in priority queues involves MATH!

P = Parent
2P = Left Child
2P + 1 = Right Child

We can find a parent by doing n//2 where n is the child node.

"""


class BinaryHeap:
    """
        This is a min_heap implementation.
    """

    def __init__(self):
        # put a dummy value into spot 0 to make integer division easier later.
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1

    def add(self, item):
        pass

    def bubble_up(self):
        i = len(self)
        while i // 2 > 0:
            # check that the newly added item doesn't have a value less than its parent.
            if self.items[i] < self.items[i // 2]:
                # if it does, swap them.
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
            # move 'up' the tree to the parent and keep checking.
            i = i // 2

    def insert(self, k):
        self.items.append(k)
        self.bubble_up()

    def bubble_down(self, i):
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.items[i] > self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > len(self):
            return i * 2

        if self.items[i * 2] < self.items[i * 2 + 1]:
            return i * 2

        return i * 2 + 1

    def delete_min(self):
        # have to use [1], since we're using a dummy val for [0]
        return_val = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.bubble_down(1)
        return return_val

    def build_heap(self, alist):
        i = len(alist) // 2
        self.items = [0] + alist
        while i > 0:
            self.bubble_down(i)
            i = i - 1