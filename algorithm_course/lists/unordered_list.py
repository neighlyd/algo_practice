class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        """
            Add a node to the BEGINNING of the list.
        :param item: Node object
        :return: nothing
        """
        i_node = Node(item)
        i_node.next = self.head
        self.head = i_node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def search(self, item):
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        # ASSUMES ITEM IS IN LIST!!
        current = self.head
        prev = None

        while True:
            if current.value == item:
                break
            prev, current = current, current.next

        # Check if the first node is the one being deleted.
        if prev is None:
            self.head = current.next
        else:
            # Otherwise, update the previous node's next val with the current node's next val.
            prev.next = current.next

    def append(self, item):
        i_node = Node(item)
        if not self.head:
            self.head = i_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = i_node

    def index(self, item):
        idx = 0
        current = self.head
        while current is not None:
            if current.value == item:
                return idx
            idx += 1
            current = current.next

    def pop(self):
        current = self.head
        prev = None
        while current.next is not None:
            prev, current = current, current.next
        prev.next = None
        return current

    def insert(self, idx, item):
        i_node = Node(item)
        current = self.head
        prev = None
        idx_count = 0
        while idx != idx_count:
            prev, current = current, current.next
            idx_count += 1
        if prev is not None:
            prev.next = i_node
        i_node.next = current

    def display_nodes(self):
        current = self.head
        r = f'{current.value}'
        while current.next is not None:
            current = current.next
            r += f' => {current.value}'
        return r


ul = UnorderedList()
print(f'Starting with an empty Unordered List: {ul.is_empty()}')
print('adding 3')
ul.append(3)
print(ul.display_nodes())
print(f'The Unordered List is no longer empty: {ul.is_empty()}')
print('adding 2, shifting list right')
ul.add(2)
print(ul.display_nodes())
print('adding 1, shifting list right')
ul.add(1)
print(ul.display_nodes())
print(f'The list should be size 3: {ul.size()}')
print('index of 2 is', ul.index(2))
print('popping last element:', ul.pop().value)
print(ul.display_nodes())
print('inserting 4 at position 2')
ul.insert(2, 4)
print(ul.display_nodes())
print('appending 6 to end of list')
ul.append(6)
print(ul.display_nodes())
