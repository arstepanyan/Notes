# Implement an algorithm that takes as input an array of distinct elements and size,
# and returns a subset of the given size of the array elements.
# All subsets should be equally likely. Return the result in input array itself.
import random

# We begin by choosing one element at random from the entire array.
# We repeat the same process with the n-1 element subarray A[1, n-1].
# Eventually, the random subset occupies the slots A[0, k-1] and the remaining elements are in the last n-k slots.
# A(k) time complexity
# O(1) additional space complexity
def random_subset(A, k):
    """
    Random subset generator
    :param A: List[unique int]
    :param k: size of the subset
    :return: A modified so that the first k elements are the random subset
    """
    for i in range(k):
        random_number = random.randint(i, len(A) - 1)
        A[random_number], A[i] = A[i], A[random_number]
    return A


if __name__ == "__main__":
    A = [3, 7, 5, 11]
    k = 3
    print(random_subset(A, k))