"""
    Implement a function to check if a linked list is a palindrome.
    You can know the length of the list.
"""
from linked_list import LinkedList


def palindrome(ul):
    # use a regular list as a stack to track first half of the linked_list.
    # If we allowed imports, a dequeue could also be used,
    # but since we're only using the end of the stack, it's not a performance issue.
    first_half = []
    mid_point = len(ul) // 2
    i = 0
    curr = ul.head
    # populate the first half of the linked list into the stack we made.
    while i < mid_point:
        first_half.append(curr)
        curr = curr.next
        i += 1
    # We are now at the mid-point of our linked list.
    # If the list is odd, we need to skip over the middle char.
    if (len(ul) % 2) != 0:
        curr = curr.next
    while curr:
        backwards = first_half.pop()
        if curr.val != backwards.val:
            return False
        else:
            curr = curr.next
    return True

not_pal = LinkedList()

not_pal.append('a')
not_pal.append('b')
not_pal.append('c')
not_pal.append('a')
assert palindrome(not_pal) is False

pal_even = LinkedList()
pal_even.append('a')
pal_even.append('b')
pal_even.append('b')
pal_even.append('a')
assert palindrome(pal_even) is True

pal_odd = LinkedList()
pal_odd.append('a')
pal_odd.append('b')
pal_odd.append('q')
pal_odd.append('b')
pal_odd.append('a')
assert palindrome(pal_odd) is True