class ListNode:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print('List is empty')
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


def cyclicity(L):
    fast = slow = L.head
    while fast and fast.next and fast.next.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            # Find the start of the cycle
            length = cycle_len(fast)
            node2 = L.head
            for i in range(length):
                node2 = node2.next
            node1 = L.head
            while node1 != node2:
                node1, node2 = node1.next, node2.next
            return node1
    return None


def cycle_len(node):
    beg, len = node, 0
    while True:
        len += 1
        beg = beg.next
        if beg == node:
            return len


if __name__ == '__main__':
    # Create a linked list with a cycle
    l1 = LinkedList()
    l1.insert(ListNode(1))
    l1.insert(ListNode(5))
    l1.insert(ListNode(7))
    l1.insert(ListNode(0))
    l1.insert(ListNode(4))
    lastNode = ListNode(8)
    lastNode.next = l1.head.next.next
    l1.insert(lastNode)

    # NOTE: As we intentiannaly added a cycle in this linked list,
    #       the printing will be infinite.
    #       Either don't print it (means that you should leave the following line as is, do not uncomment them)
    #       or manually stop the printing before I modify the code
    print('L1')
    # l1.printList()
    cycle_exists = cyclicity(l1)
    if cycle_exists:
        print(f'The beginning node of the cycle ... {cycle_exists.data}\n')
    else:
        print('There is no cycle in the list\n')

    # Create a linked list without a cycle
    l2 = LinkedList()
    l2.insert(ListNode(1))
    l2.insert(ListNode(5))
    l2.insert(ListNode(7))
    l2.insert(ListNode(0))
    l2.insert(ListNode(4))
    l2.insert(ListNode(8))
    print('L2')
    l2.printList()
    cycle_exists = cyclicity(l2)
    if cycle_exists:
        print(f'The beginning node of the cycle ... {cycle_exists.data}\n')
    else:
        print('There is no cycle in the list\n')
