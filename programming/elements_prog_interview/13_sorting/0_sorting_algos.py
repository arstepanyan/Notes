# O(n^2) time complexity
def bubble_sort1(l):
    """
    Sorts l
    :param l: List[int], will work on strings as well
    :return: sorted l
    """
    i, j = 0, len(l)
    while i < j:
        while i + 1 < j:
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
            i += 1
        j -= 1
        i = 0
    return l


# O(n^2) time complexity. Slightly faster than the above because there is a stopping condition
def bubble_sort2(l):
    """
    Sorts l
    :param l: List[int], will work on strings as well
    :return: sorted l
    """
    i, j = 0, len(l)
    swap = False
    while not swap:  # stop whenever there are no swaps made
        swap = True
        while i + 1 < j:
            if l[i] > l[i + 1]:
                swap = False
                l[i], l[i + 1] = l[i + 1], l[i]
            i += 1
        j -= 1
        i = 0
    return l


# O(n^2) time complexity
def selection_sort(l):
    """
    Sorts l
    :param l: List[int], will work on strings as well.
    :return: sorted l
    """
    i = 0
    while i < len(l):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
        i += 1
    return l


# O(n log n) time complexity, additional O(n) space complexity
def merge_sort(l):
    """
    sort l
    :param l: List[int], will work on strings as well
    :return: sorted l
    """
    if len(l) < 2:
        return l
    else:
        middle = len(l) // 2
        l1 = merge_sort(l[: middle])
        l2 = merge_sort(l[middle:])
        return _merge(l1, l2)


def _merge(l1, l2):
    """
    merge l1 and l2
    :param l1: List[]
    :param l2: List[]
    :return: merged l1 and l2
    """
    p1, p2 = 0, 0
    res = []
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            res.append(l1[p1])
            p1 += 1
        else:
            res.append(l2[p2])
            p2 += 1

    while p1 < len(l1):
        res.append(l1[p1])
        p1 += 1

    while p2 < len(l2):
        res.append(l2[p2])
        p2 += 1

    return res


if __name__ == "__main__":
    import time
    import random

    print('Bubble sort without stopping condition: ', selection_sort([0, 4, 100, -10]))
    print('Bubble sort with stopping condition: ', selection_sort([0, 4, 100, -10]))
    print('Selection sort: ', selection_sort([0, 4, 100, -10]))
    print('Merge sort: ', selection_sort([0, 4, 100, -10]))

    l = [random.randint(-100, 100) for i in range(10000)]
    t0 = time.time()
    bubble_sort1(l)
    print(f'Bubble sort without stopping condition ............... {time.time() - t0} seconds')

    l = [random.randint(-100, 100) for i in range(10000)]
    t0 = time.time()
    bubble_sort2(l)
    print(f'Bubble sort stopping whenever there are no swaps ..... {time.time() - t0} seconds')

    l = [random.randint(-100, 100) for i in range(10000)]
    t0 = time.time()
    selection_sort(l)
    print(f'\nSelection_sort ....................................... {time.time() - t0} seconds')

    l = [random.randint(-100, 100) for i in range(10000)]
    t0 = time.time()
    merge_sort(l)
    print(f'Merge sort ........................................... {time.time() - t0} seconds')
