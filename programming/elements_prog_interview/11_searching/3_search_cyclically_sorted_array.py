# Design an O(log n) algorithm for finding the position of the samllest element in a cyclically sorted array.
# Assume all elements are distinct.
# For example, for the array [378, 478, 550, 631, 103, 203, 220, 234, 279, 368], the answer is 4
def smallest(L):
    left, right = 0, len(L) - 1
    while left < right:
        middle = left + (right - left) // 2
        if L[middle] < L[right]:
            right = middle
        elif L[middle] >= L[left]:
            left = middle + 1
    # Loop ends when left == right
    return left

if __name__ == '__main__':
    print(smallest([378, 478, 550, 631, 103, 203, 220, 234, 279, 368]))
