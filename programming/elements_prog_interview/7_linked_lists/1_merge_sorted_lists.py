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


def merge_two_sorted_lists(L1, L2):
    # Create a placeholder for the result
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next


def printMerged(node):
    while True:
        if node is None:
            break
        print(node.data)
        node = node.next


if __name__ == '__main__':
    # Create the first ordered linked list and print
    l1 = LinkedList()
    l1.insert(ListNode(1))
    l1.insert(ListNode(6))
    print('L1')
    l1.printList()

    # Create the second ordered linked list and print
    l2 = LinkedList()
    l2.insert(ListNode(2))
    l2.insert(ListNode(4))
    l2.insert(ListNode(11))
    print('\n\nL2')
    l2.printList()

    # Merge the two lists and print
    merged_list = merge_two_sorted_lists(l1.head, l2.head)
    print('\nMerged')
    printMerged(merged_list)
