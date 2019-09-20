def first_occurance(L, v):
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


def last_occurance(L, v):
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


def interval_inclosing_key(L, k):
    first = first_occurance(L, k)
    last = last_occurance(L, k)
    return [first, last]


if __name__ == "__main__":
    print(first_occurance([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285))
    print(interval_inclosing_key([1, 2, 2, 4, 4, 4, 7, 11, 11, 13], 11))
