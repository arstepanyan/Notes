def bsearch(L, v):
    """
    Binary search
    :param L: List[int]
    :param v: int
    :return: -1 if v not in the list, else the index of v
    """
    left, right = 0, len(L) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if L[middle] < v:
            left = middle + 1
        elif L[middle] == v:
            return middle
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    print(bsearch([1, 5 , 7, 9, 20, 100], 9))