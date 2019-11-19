"""
The International Standard Book Number (ISBN) is a unique commercial book identifier.
It is a string of length 10. The first 9 characters are digits; the last character is a check character.
The check character is the sum of the first 9 digits, mod 11, with 10 represented by 'X'.
(Modern ISBNs use 13 digits, and the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs).

Create a cache for looking up prices of books identified by their ISBN.
For the purpose of this exercise, treat ISBNs and prices as positive integers.
You must implement lookup, insert, and erase methods. Use the Least Recently Used (LRU) policy for cache eviction.

* Insert: If an ISBN is already present, insert should not update the price, but should update the ISBN to be the most recently used entry.
* Lookup: given an ISBN ,return the corresponding price; if the element is not present, return -1.
If ISBN is present, update that entry to be the most recently used ISBN.
* Erase: remove the specified ISBN and corresponding value from the case. Return true if the ISBN was present; otherwise, return false.
"""

# Ordered dictionary solution
# Time for lookup and update = O(1)
import collections
class ISBMCache:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity


    def insert(self, key, value):
        if key in self.cache:
            value = self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


    def lookup(self, key):
        if key not in self.cache:
            return -1
        price = self.cache.pop(key)
        self.cache[key] = price
        return price


    def erase(self, key):
        return self.cache.pop(key, None) is not None



# Doubley linked list solution
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


if __name__ == "__main__":
    cache = ISBMCache(3)
    cache.insert(1, 11)
    cache.insert(2, 8)
    cache.insert(3, 20)

    print(cache.cache)
    print(cache.lookup(2))
    print(cache.cache)

    cache.insert(4, 30)
    print(cache.cache)

    print(cache.erase(1))
    print(cache.cache)

    print(cache.erase(4))
    print(cache.cache)