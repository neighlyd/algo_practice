class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val}'


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def _node_check(self, val):
        """
            Checks if a given object is a Node instance or not. If not, turns the value into a Node object.
        :param val: Any given object.
        :return: A Node
        """
        if isinstance(val, Node):
            return val
        else:
            return Node(val)

    def add(self, val):
        """
            Adds a node to the BEGINNING of the list.
        :param val: value to be added to the list.
        :return: None
        """
        node = self._node_check(val)
        node.next = self.head
        self.head = node

    def append(self, val):
        """
            Append a new node to the END of the list. If no elements in list, it adds element as head.
        :param val: Value to insert into node.
        :return: None
        """
        node = self._node_check(val)
        if self.is_empty():
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def index(self, val):
        """
            Find the index of a value in the list.
        :param val: Vale of node to locate
        :return: Int - index value of node to locate.
        """
        curr = self.head
        counter = 0
        while curr:
            if curr.val == val:
                return counter
            counter += 1
            curr = curr.next
        return -1

    def insert(self, val, idx):
        """
            Attempt to insert the node at a specific index location.
            If that location is not in the list, the node will not be added.
        :param val: Value of node to be inserted.
        :param idx: Index location of node to be added
        :return: None
        """
        node = self._node_check(val)
        curr = self.head
        prev = None
        count = 0
        while count != idx:
            prev, curr = curr, curr.next
            count += 1
        if prev is not None:
            prev.next = node
        node.next = curr

    def peak(self):
        return self.head.val

    def pop(self):
        """
            Remove the last node from the list and return it to the user.
        :return: Node - the last node from the list.
        """
        curr = self.head
        prev = None
        # walk to the end of the list.
        while curr.next is not None:
            prev, curr = curr, curr.next

        # Remove the .next from the penultimate node and return the last node.
        prev.next = None
        return curr

    def search(self, val):
        """
            Checks to see if a node is in the list.
        :param val: Value of node
        :return: Boolean - present or absent
        """
        if self.is_empty():
            return False
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    @property
    def size(self):
        """
            Return the total number of nodes in the list by traversing the full list.
        :return: Int - number of nodes in list.
        """
        counter = 0
        curr = self.head
        while curr:
            counter += 1
            curr = curr.next
        return counter

    def remove(self, val):
        """
            Removes a given item from the list, if it is present.
        :param val: Values to remove from list
        :return: None
        """
        if self.is_empty():
            return None
        curr = self.head
        if curr.val == val:
            self.head = curr.next
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
                return None
            curr = curr.next
        return None

    def __str__(self):
        curr = self.head
        r = f'{curr.val}'
        while curr.next is not None:
            curr = curr.next
            r += f' => {curr.val}'
        return r

    def __len__(self):
        return self.size()


def test_list():
    ul = LinkedList()
    assert ul.is_empty() is True
    ul.append(3)
    assert ul.is_empty() is False
    assert ul.size == 1
    assert len(ul) == 1
    assert ul.peak() == 3
    ul.add(2)
    assert ul.peak() == 2
    ul.append(6)
    assert ul.size == 3
    assert len(ul) == 3
    assert ul.pop().val == 6
    assert ul.size == 2
    assert len(ul) == 2
    ul.append(5)
    ul.remove(3)
    assert ul.size == 2
    assert len(ul) == 2
    ul.insert(4, 1)
    assert ul.size == 3
    assert len(ul) == 3
    assert ul.index(4) == 1
    ul.insert(4, 16)
    assert ul.size == 3
    assert len(ul) == 3
