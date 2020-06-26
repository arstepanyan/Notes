"""
Leetcode 232. Implement Queue using Stacks

Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Example:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

# Time: Amortized time for each operation O(1)
# Aux Space: O(n) (2 stacks solution below. 1 stack solution with recursion when pushing is also possible)
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_enqueue = []
        self.stack_dequeue = []
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_enqueue.append(x)
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size == 0:
            return False

        if self.stack_dequeue == []:
            for _ in range(self.size):
                self.stack_dequeue.append(self.stack_enqueue.pop())
        self.size -= 1
        return self.stack_dequeue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.size == 0:
            return False
        if self.stack_dequeue == []:
            for _ in range(self.size):
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())  # returns 1
    queue.pop()  # returns 1
    print(queue.empty())  # returns false
