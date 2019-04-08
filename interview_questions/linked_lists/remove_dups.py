"""
    Write code to remove duplicates from an unsorted linked list.
"""
from linked_list import LinkedList


def remove_dups(linked):
    """
        Removes duplicated elements from a linked list.
    :param linked: Linked List object.
    :return: None
    """
    dups = set()
    curr = linked.head
    prev = None
    while curr:
        if curr.val in dups:
            prev.next = curr.next
            curr = prev.next
        else:
            dups.add(curr.val)
            prev, curr = curr, curr.next


l = LinkedList()
l.add(1)
l.add(1)
l.add(2)
l.add(3)
l.add(1)
l.add(5)
l.add(3)
l.add(6)
l.add(6)
print(l)

remove_dups(l)
print(l)