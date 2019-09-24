# Write a program which takes as input two sorted arrays of integers, and updates the first to the combined entries
# of the two arrays in sorted order. Assume the first array has enough empty entries at its end to hold the results.

# O(m + n) time complexity, O(1) additional space complexity
def merge_sorted_arrays(l1, m, l2, n):
    """
    Merges two sorted arrays
    :param l1: List[int]
    :param m: length of l1 (not counting the 0s at the end of the array)
    :param l2: List[int]
    :param n: length of l2
    :return: merged l1 and l2
    """
    for el in l2:
        hole = m
        print(l1)
        i = hole - 1

        while i != 0 and l1[i] > el:
            l1[hole] = l1[i]
            i -= 1
            hole -= 1
        l1[hole] = el
        m = m + 1

    return l1

if __name__ == "__main__":
    l1 = [3, 13, 17, 0, 0, 0, 0, 0]
    l2 = [3, 7, 11, 19]

    print(merge_sorted_arrays(l1, 3, l2, 4))