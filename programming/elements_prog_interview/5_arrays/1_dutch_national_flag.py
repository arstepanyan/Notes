# Time complexity = O(n), space complexity = O(1)
def dutch_flag1(A, i):
    """
     Rearrange the elements of A such that all elements less than A[i] (the 'pivot') appear first,
         followed by elements equal to the pivot, followed by elements greater than the pivot
    :param A: list
    :param i: index of the pivot
    :return: list
    """
    pivot = A[i]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    return A

# The same complexities but with one pass
def dutch_flag2(A, i):
    pivot = A[i]
    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
            #larger -= 1
    return A

if __name__ == "__main__":
    print(dutch_flag1([0,1,2,0,2,1,1], 2))
    print(dutch_flag2([0,1,2,0,2,1,1], 2))
