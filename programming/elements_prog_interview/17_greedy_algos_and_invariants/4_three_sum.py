"""
Design an algorithm that takes as input an array and a number, and determines if there are three entries in the array
(not necessarily distinct) which add up to the specified number.
For example, in [11, 2, 5, 7, 3] there are three numbers that add up to 21 ([3, 7, 11] and [5, 5, 11]).
However, no three entries add up to 22.
"""


# Time = O(n)
# Space = O(1)
def two_sum(array, target):
    beg, end = 0, len(array) - 1

    while beg <= end:
        if array[beg] + array[end] == target:
            return True
        elif array[beg] + array[end] < target:
            beg += 1
        else:
            end -= 1
    return False


# Time = O(n^2)
# Space = O(1)
def three_sum(array, target):
    array.sort()
    for i, el in enumerate(array):
        if two_sum(array, target - el):
            return True
    return False


if __name__ == "__main__":
    print(three_sum([11, 2, 5, 7, 3], 22))
