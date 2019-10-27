# Without knowing the length of a linked list, delete the kth last element in a singly linked list.

from collections import deque


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time = O(n), Extra Space = (k)
def remove_kth(l, k):
    head = l
    q = deque()
    for _ in range(k + 1):
        q.append(l)
        l = l.next

    while l:
        q.append(l)
        q.popleft()
        l = l.next

    q[0].next = q[0].next.next
    return head


# Time = O(n), Extra Space = O(1)
def remove_kth2(l, k):
    dummy = Node(l.val, l)
    first, second = dummy.next, dummy

    # Advance the first pointer by k
    for _ in range(k):
        first = first.next

    # Advance both pointers in tandem
    while first:
        first, second = first.next, second.next

    # second pointer points at the (k+1)th last element
    second.next = second.next.next

    return dummy.next


if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(5)
    l1.next.next = Node(6)
    l1.next.next.next = Node(8)
    l1.next.next.next.next = Node(9)

    l1 = remove_kth(l1, 3)
    while l1:
        print(l1.val)
        l1 = l1.next

    print('........')

    l1 = Node(1)
    l1.next = Node(5)
    l1.next.next = Node(6)
    l1.next.next.next = Node(8)
    l1.next.next.next.next = Node(9)

    l1 = remove_kth2(l1, 3)
    while l1:
        print(l1.val)
        l1 = l1.next
