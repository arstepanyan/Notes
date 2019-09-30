# Write a program which takes as input an array of digits encoding a nonnegative decimal integer D
# and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

# Time complexity = O(n) where n is the number of elements in the array
def increment_by_one(D):
    """
    Increment by 1
    :param D: List[int]
    :return: List[int]
    """
    for i in range(len(D)):
        if D[-i - 1] == 9:
            D[-i - 1] = 0
            if i == len(D) - 1:
                # D.insert(0, 1)
                # Instead of inserting 1 in the position 0, we can do the following
                D[0] = 1
                D.append(0)
        else:
            D[-i - 1] += 1
            break
    return D


if __name__ == "__main__":
    D1 = [1, 2, 9]
    D2 = [9, 9, 9]
    print(increment_by_one(D1))
    print(increment_by_one(D2))