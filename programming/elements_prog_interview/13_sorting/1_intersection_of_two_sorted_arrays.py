# write a program which takes as input two sorted arrays, and returns a new array containing elements that are present
# in both of the input array. The input arrays may have duplicate entries, but the returned array should be free of duplicates.

# O(m + n) time complexity, as adding an element to a set is O(1)
def intersection(l1, l2):
    """
    computes the intersection of l1 and l2
    :param l1: List[int]
    :param l2: List[int]
    :return: set, intersection of l1 and l2
    """
    p1, p2 = 0, 0
    res = set()

    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            p1 += 1
        elif l1[p1] == l2[p2]:
            res.add(l1[p1])
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    return res


# O(m + n), from the book, faster than above
def intersect_two_sorted_arrays(A, B):
    """
    Computes the intersection of A and B
    :param A: List[int]
    :param B: List[int]
    :return: List[int], intersection of A and B
    """
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_A_B


if __name__ == "__main__":
    import time

    l1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12, 100, 300, 301, 301, 400, 400, 410, 412, 423, 425]
    l2 = [5, 5, 6, 8, 8, 9, 10, 10]

    t0 = time.time()
    print(intersection(l1, l2))
    print(f'Intersection(l1, l2) ......... {time.time() - t0}')

    t0 = time.time()
    print(intersect_two_sorted_arrays(l1, l2))
    print(f'Intersect_two_sorted_arrays(t1, t2) ...... {time.time() - t0}')
