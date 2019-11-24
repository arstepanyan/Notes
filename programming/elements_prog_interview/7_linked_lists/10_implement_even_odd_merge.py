"""
Write a program that computes the even-odd merge.

Define the even-odd merge of singly linked list to be the list consisting of the even-numbered nodes
followed by the odd-numbered nodes.

Input: L -> l0 -> l1 -> l2 -> l3 -> l4
Output: L -> l0 -> l2 -> l4 -> l1 -> l3

Do not create a new list.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Time = O(n)
# Space = O(n)
def even_odd_merge(l):
    if not l or not l.next:
        return l

    p1, head2, p2 = l, l.next, l.next

    count = 0  # to keep track of the node number tht p1 is pointing at
    while p1.next.next:
        p1.next = p1.next.next
        p2, p1 = p1.next, p2
        count += 1

    if count % 2 == 0:  # p1 is pointing to an even numbered node
        p1.next = head2
    else:  # p1 is pointing to an odd numbered node
        p2.next = head2
        p1.next = None
    return l


if __name__ == "__main__":
    l = ListNode(0)
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(3)

    even_odd_merge(l)
    res1 = []
    while l:
        res1.append(l.val)
        l = l.next

    l = ListNode(0)
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(3)
    l.next.next.next.next = ListNode(4)

    even_odd_merge(l)
    res2 = []
    while l:
        res2.append(l.val)
        l = l.next

    print(res1, res2)
