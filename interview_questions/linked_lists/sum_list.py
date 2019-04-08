"""
    Given two numbers represented by two linked lists, where each node contains a single digit sorted in reverse order
    (such that the 1s digit is the head), sum the lists together.

    E.G:

        list_one = [7 -> 1 -> 6]
        list_two = [5 -> 9 -> 2]
        output = [2 -> 1 -> 9]

    Constraints: Do not just convert the lists to an integer.
"""
from linked_list import LinkedList


def sum_list(n, m):
    print(f"n is: {n}\nm is: {m}")
    res = LinkedList()
    n_p = n.head
    m_p = m.head
    carry = 0
    while n_p is not None or m_p is not None or carry != 0:
        if n_p:
            n_v = n_p.val
        else:
            n_v = 0
        if m_p:
            m_v = m_p.val
        else:
            m_v = 0
        total = n_v + m_v + carry
        print(f"Total is {total}")
        carry = total // 10
        res.append(total % 10)
        if n_p:
            n_p = n_p.next
        if m_p:
            m_p = m_p.next
    return res

n = LinkedList()
n.add(6)
n.add(1)
n.add(7)
n.add(5)

m = LinkedList()
m.add(2)
m.add(9)
m.add(5)

print(sum_list(n, m))
