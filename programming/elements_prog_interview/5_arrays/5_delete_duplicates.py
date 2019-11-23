"""
Write a program that takes as input a sorted array and updates it so that all duplicates have been removed
and the remaining elements have been shifted left to fill the emptied indices.
Return the number of valid elements.
For example, if the input array is [2,3,5,5,7,11,11,11,13], after deletion it will be [2,3,5,7,11,13,11,11,13]
and the program should return 6.
"""


# Time = O(n)
# Space = O(1)
def delete_duplicates(array):
    prev_i = 0
    for i, el in enumerate(array[1:]):
        if el != array[prev_i]:
            array[prev_i + 1] = el
            prev_i += 1
    return None if prev_i == 0 else prev_i + 1


if __name__ == "__main__":
    print(delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]))
