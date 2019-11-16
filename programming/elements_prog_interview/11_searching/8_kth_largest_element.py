# Design an algorithm for computing the kth largest element in an array
import heapq


# time complexity = O(n log k)
# extra space complexity = O(k)
def kth_largest(L, k):
    k_largest = L[:k]
    heapq.heapify(k_largest)  # min heap
    for el in L[k:]:
        if el >= k_largest[0]:
            heapq.heappushpop(k_largest, el)
    return k_largest[0]


# Time complexity = O(n)
#      Explanation: Since we expect to reduce the number of elements to process bby roughly half,
#      the average time complexity T(n) satisfies T(n) = O(n) + T(n/2). This solves to O(n).
#      The worst case time-complexity is O(n^2), which occurs when the randomly selected pivot
#      is the smallest or largest element in the current subarray. The probability of the worst case
#      reduces exponentially with the length of the input array, and the worst case is a nonissue in practice.
#      For this reason, the randomize selection algorithm is sometimes said to have almost certain O(n) time complexity.
# Additional Space = O(1)
import random


def kth_largest_2(s, k):
    left, right = 0, len(s) - 1
    while left <= right:
        cur_pivot_indx = random.randint(left, right - 1)
        new_pivot_indx = partition_around_pivot(s, left, right, cur_pivot_indx)
        if new_pivot_indx == k - 1:
            return s[new_pivot_indx]
        elif new_pivot_indx > k - 1:
            right = new_pivot_indx - 1
        else:
            left = new_pivot_indx + 1


def partition_around_pivot(s, left, right, cur_pivot_indx):
    pivot_val = s[cur_pivot_indx]
    new_pivot_indx = left
    s[right], s[cur_pivot_indx] = s[cur_pivot_indx], s[right]
    for i in range(left, right):
        if s[i] >= pivot_val:
            s[i], s[new_pivot_indx] = s[new_pivot_indx], s[i]
            new_pivot_indx += 1
    s[right], s[new_pivot_indx] = s[new_pivot_indx], s[right]
    return new_pivot_indx


if __name__ == "__main__":
    print(kth_largest([3, 2, 1, 5, 4, 4], 3))
    print(kth_largest_2([3, 2, 1, 5, 4], 4))
