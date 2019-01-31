from .unordered_list import Node, UnorderedList


class OrderedList(UnorderedList):

    def search(self, item):
        # Takes advantage of the fact that the list is ordered. Once current is larger than the amount we're searching
        # for, we know we will never find it.
        # Not as efficient as a binary search, but it's useful for demonstration purposes.
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            elif current.value > item:
                return False
            current = current.next
        return False

    def add(self, item):
        i_node = Node(item)
        current = self.head
        prev = None

        while current is not None:
            if current.value > item.value:
                break
            previous, current = current, current.next

        if prev is None:
            i_node.next, self.head = self.head, i_node
        else:
            i_node.next, prev.next = current, i_node

    def append(self, item):
        # There is no implementation of append in an Ordered List
        pass

    def insert(self, idx, item):
        # There is no implementation of insert in an Ordered List
        pass