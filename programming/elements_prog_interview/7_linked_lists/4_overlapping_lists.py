"""
Given two singly linked lists there may be list nodes that are common to both.
(This may not be a bug - it may be desirable from the perspective of reducing memory footprint,
as in the flyweight pattern, or maintaining a canonical form).
Write a program that takes two cycle-free singly linked lists, and determines if there exists a node that is common to both lists.
"""


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def common_list(l1, l2):
    # Find the lengths of the lists
    def length(l):
        ans = 0
        while l:
            ans += 1
            l = l.next
        return ans

    len_l1, len_l2 = length(l1), length(l2)
    if len_l1 > len_l2:
        l1, l2 = l2, l1  # l2 is the longer list

    # Advance through the longer list by the difference in length
    for _ in range(abs(len_l1 - len_l2)):
        l2 = l2.next

    # Advance through both lists in tandem, stopping at the first common node
    while l1 and l2 and l1.val != l2.val:
        l1, l2 = l1.next, l2.next

    return l1.val if l1 else l1  # None if their reached the end without finding any comomn node


if __name__ == "__main__":
    l1 = Node(1)
    l1.next = Node(5)
    l1.next.next = Node(6)
    l1.next.next.next = Node(8)
    l1.next.next.next.next = Node(9)
    l2 = Node(2)
    l2.next = Node(7)
    l2.next.next = Node(8)
    l2.next.next.next = Node(9)

    print(common_list(l1, l2))

    print('.................')
    l1 = Node(1)
    l1.next = Node(5)
    l1.next.next = Node(6)
    l1.next.next.next = Node(8)
    l1.next.next.next.next = Node(9)
    l2 = Node(2)
    l2.next = Node(7)
    l2.next.next = Node(10)

    print(common_list(l1, l2))
