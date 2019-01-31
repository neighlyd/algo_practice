"""
    Heap as binary Tree Structure of Heaps:
    Node = i
    Parent = i/2
    Left Child = 2i
    Right Child = 2i + 1

    Max Heap:
    Key of a Node >= Keys of its Children.

    Min Heap:
    Key of a Node <= Keys of its Children.
"""


class MaxHeap:

    def __init__(self, items=None):
        self.heap = []
        if items:
            for i in items:
                self.push(i)

    def peek(self):
        if len(self.heap) >= 1:
            return self.heap[0]
        else:
            return False

    def push(self, x):
        self.heap.append(x)
        if len(self.heap) > 1:
            idx = len(self.heap) - 1
            self.bubble_up(idx)

    def extract(self):
        if len(self.heap) == 0:
            return False
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            last = len(self.heap) - 1
            self.swap(0, last)
            max_val = self.heap.pop()
            self.bubble_down(0)
            return max_val

    def bubble_up(self, idx):
        if idx != 0 and self.heap[idx] > self.heap[idx//2]:
                self.swap(idx, idx//2)
                self.bubble_up(idx//2)

    def bubble_down(self, idx):
        # Also called "max_heapify" in some text books (e.g. Introduction to Algorithms)
        if idx == 0:
            if len(self.heap) > 1 and self.heap[1] > self.heap[0]:
                self.swap(0, 1)
                self.bubble_down(1)
            if len(self.heap) > 2 and self.heap[2] > self.heap[0]:
                self.swap(0, 2)
                self.bubble_down(2)
        else:
            left = idx*2
            right = idx*2+1
            largest = idx
            if self.has_left_child(idx) and self.heap[left] > self.heap[idx]:
                largest = left
            if self.has_right_child(idx) and self.heap[right] > self.heap[idx]:
                largest = right
            if largest != idx:
                self.swap(idx, largest)
                self.bubble_down(largest)

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def has_right_child(self, idx):
        return idx*2+1 < len(self.heap)

    def has_left_child(self, idx):
        return idx*2 < len(self.heap)


arr = [12, 3, 155, 451, 88, 9]

m = MaxHeap(arr)
print(m.peek())
m.push(556)
print(m.peek())
print(m.extract())
print(m.peek())