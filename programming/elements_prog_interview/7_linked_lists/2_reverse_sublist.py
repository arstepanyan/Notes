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

def reverse_sublist(L, s, f):
    # Find the element preceding the first element of the sublist
    prev = L.head
    for i in range(s-2):
        prev = prev.next

    # First element of the sublist
    first = prev.next

    # Last element of the sublist
    last = L.head
    for i in range(f-1):
        last = last.next

    # Reverse
    for i in range(f-s):
        prev.next = first.next
        first.next = last.next
        last.next = first
        first = prev.next
    return L

if __name__ == '__main__':
    # Create a list and print
    l = LinkedList()
    l.insert(ListNode(11))
    l.insert(ListNode(3))
    l.insert(ListNode(5))
    l.insert(ListNode(7))
    l.insert(ListNode(2))
    print('L')
    l.printList()

    # Reverse sublist containing elements from 2nd to 4th positions
    reversed = reverse_sublist(l, 2, 4)
    print('\nReversed')
    LinkedList.printList(reversed)






