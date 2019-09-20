def first_occurrance(L, v):
    """
    Find the first occurence of v in L
    :param L: List[int]
    :param v: int
    :return: -1 if v is not in the list, else the index of the first occurrence of v
    """
    if L[0] == v:
        return 0

    left, right = 0, len(L) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if L[middle] >= v:
            right = middle - 1
        else:
            left = middle + 1
            if L[left] == v:
                return left
    return -1


def last_occurrance(L, v):
    """
    Find the last occurence of v in L
    :param L: List[int]
    :param v: int
    :return: -1 if v is not in the list, else the index of the last occurrence of v
    """
    if L[-1] == v:
        return len(L) - 1

    left, right = 0, len(L) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if L[middle] <= v:
            left = middle + 1
        else:
            right = middle - 1
            if L[right] == v:
                return right
    return -1


def interval_enclosing_key(L, k):
    """
    Find the interval enclosing k
    :param L: List[int]
    :param k: int
    :return: -1 if k is not in L, else the indices of the first and the last occurrences of k
    """
    first = first_occurrance(L, k)
    last = last_occurrance(L, k)
    return [first, last]


if __name__ == "__main__":
    print(first_occurrance([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285))
    print(interval_enclosing_key([1, 2, 2, 4, 4, 4, 7, 11, 11, 13], 1))
    print(interval_enclosing_key([2, 4, 4, 4, 4, 4, 4, 7, 11, 11, 13], 4))
