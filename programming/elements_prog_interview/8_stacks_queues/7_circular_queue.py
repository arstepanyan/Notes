"""
A queue can be implemented using an array and two additional fields, the beginning and the end indices.
This structure is sometimes referred to as a circular queue. Both enqueue and dequeue have O(1) time complexity.
If the array is fixed, there is a maximum number of entries that can be stored.
If the array is dynamically resized, the total time for m combined enqueue and dequeue operations is O(m).

Implement a queue API using an array for storing elements. Your API should include a constructor function,
which takes as argument the initial capacity of the queue, enqueue and dequeue functions,
and a function which returns the number of elements stored.
Implement dynamic resizing to support storing an arbitrarily large number of elements.
"""
class CircularQueue:
    def __init__(self, k):
        self.items = [None for _ in range(k)]
        self.start = self.end = self.size = 0


    def enqueue(self, value):
        if self.end == len(self.items):
            self.items = self.items[self.start:] + self.items[:self.start]
            self.start, self.end = 0, self.size
            self.items += [None for _ in range(len(self.items))]

        self.items[self.end] = value
        self.end += 1
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return False
        self.items[self.start] = None
        self.start += 1
        self.size -= 1

    def size(self):
        return self.size


if __name__ == "__main__":
    obj = CircularQueue(4)
    print(obj.dequeue())
    obj.enqueue(4)
    obj.enqueue(2)
    print(f'obj.items == [4, 2, None, None] ... {obj.items == [4, 2, None, None]}')
    obj.dequeue()
    print(f'obj.items == [None, 2, None, None] ... {obj.items == [None, 2, None, None]}')
    obj.enqueue(10)
    obj.enqueue(19)
    print(f'obj.items == [None, 2, 10, 19] ... {obj.items == [None, 2, 10, 19]}')
    obj.enqueue(20)
    print(f'obj.items == [2, 10, 19, 20, None, None, None, None] ... {obj.items == [2, 10, 19, 20, None, None, None, None]}')
    print('obj.items ... ', obj.items)
    print('obj.size ......', obj.size)
