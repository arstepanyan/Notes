"""
Given an array of positive integers, find the largest h
such that there are at least h entries in the array that are greater than or equal to h.
nums = [1, 7, 9, 2, 5]
h_index = 3
"""


# Time Complexity = O(n log n)
def h_index(arr):
    len_arr = len(arr)
    arr.sort()
    for i in range(len_arr):
        if arr[i] >= len_arr - i:
            return len_arr - i
    return False


if __name__ == '__main__':
    nums = [1, 7, 9, 2, 5]
    print(h_index(nums))
