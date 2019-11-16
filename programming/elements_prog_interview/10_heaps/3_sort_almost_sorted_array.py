"""
Write a program which takes as input a verty long sequence of numbers and prints the numbers in sorted order.
Each number is at most k away from its correctly sorted position.
(Such an array is sometimes referred to as being k-sorted.)
For example, no number in the sequence <3,-1,2,6,4,5,8> is more than 2 away from its final sorted position.
"""

# Time = O(n log k), insertion into min-heap is O(log n) and it has to be done for n of the elements.
# Extra spcae = O(k)
import heapq


def sort_almost_sorted(s, k):
    kheap = []
    i = 0
    while i < k:
        heapq.heappush(kheap, s[i])
        i += 1
    for i in range(len(s) - k):
        s[i] = heapq.heappushpop(kheap, s[i + k])
    s[len(s) - k:] = kheap
    return s


if __name__ == "__main__":
    print(sort_almost_sorted([3, -1, 2, 6, 4, 5, 8], 2))
