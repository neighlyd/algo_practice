"""
    Implement an algorithm to find the kth to last element of a singly linked list.
"""
from linked_list import LinkedList

def kth_element(linked, k):
    n1 = linked.head
    n2 = linked.head

    # Place n1 K elements down the list to begin with.
    for i in range(k):
        # If n1 reaches the end, then there are not K elements in the list to begin with.
        if not n1:
            return None
        n1 = n1.next

    # Walk n1 down to the end of the list. At which point, n2 will be K elements behind it by definition.
    while n1:
        n1, n2 = n1.next, n2.next
    return n2

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
print(l)

print(kth_element(l, 4))