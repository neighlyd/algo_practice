"""
    Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
    Note that the intersection is based on reference, not value.
"""
from linked_list import Node, LinkedList

def intersection(l1, l2):
    difference = max(l1.size, l2.size) - min(l1.size, l2.size)
    l1_curr = l1.head
    l2_curr = l2.head
    if l1.size > l2.size:
        while difference > 0:
            l1_curr = l1_curr.next
            difference -= 1
    else:
        while difference > 0:
            l2_curr = l2_curr.next
            difference -= 1
    while l1_curr and l2_curr:
        if l1_curr == l2_curr:
            return l1_curr
        else:
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next
    return False


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
one = Node(1)

l1_intersecting = LinkedList()
l1_intersecting.append(a)
l1_intersecting.append(b)
l1_intersecting.append(c)
l1_intersecting.append(d)
l2_intersecting = LinkedList()
l2_intersecting.append(1)
l2_intersecting.append(c)

print(l1_intersecting)
print(l2_intersecting)
print(intersection(l1_intersecting, l2_intersecting))

l2_non_intersecting = LinkedList()
l2_non_intersecting.append(1)
print('------------')
print(l2_non_intersecting)
print(intersection(l1_intersecting, l2_non_intersecting))