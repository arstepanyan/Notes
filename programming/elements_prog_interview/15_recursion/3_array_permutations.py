"""
Write a program which takes as input an array of distinct integers and generates all permutations of that array.
No permutation of the array may appear more than once.
"""

# Time = O(n n!)
# Explanation: The number of function calls, C(n) satisfies the recurrence C(n) = 1 + n C(n - 1) for n >=1, with C(0) = 1.
#              Expanding this, we see C(n) = 1 + n + n(n-1) + n(n-1)(n-2) + ... + n! = n! (1/n! + 1/(n-1)! + 1/(n-2)! + ... + 1/1!).
#              The sum (1/n! + 1/(n-1)! + 1/(n-2)! + ... + 1/1!) tends to euler's number e, so C(n) tends to (e-1) n!, i.e. , O(n!).
#              The time complexity T(n) is O(n X n!), since we do O(n) computation per call outside of the recursive calls.


def array_permute(l):
    res = []
    _array_permute(l, res, [])
    return res


def _array_permute(l, res, buff):
    if len(l) == 0:
        res.append(buff.copy())
        return
    for i in range(len(l)):
        buff.append(l[i])
        _array_permute(l[i + 1:] + l[:i], res, buff)
        buff.pop()


if __name__ == "__main__":
    print(array_permute([1, 2]))
    print(array_permute([1, 2, 3]))
    print(array_permute([1, 2, 3, 4]))

