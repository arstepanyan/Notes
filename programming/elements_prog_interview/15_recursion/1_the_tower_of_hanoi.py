'''
A peg contains rings in sorted order, with the largest ring being the lowest.
You are to transfer these rings to another peg, which is initially empty.
You have a third peg, which is initially empty.
The only operation you can perform is taking a single ring from the top of one peh and placing it on the top of another peg.
You must never place a larger ring above a smaller ring.
Write a function which returns a sequence of operations that result in the transfer of n rings from one peg to another.
Each operation should be encoded as a pair (from_peg, to_peg)
'''

# Time = O(2^n)
# Explanation: The number of moves, T(n), satisfies the following recurrence: T(n) = T(n-1) + 1 + T(n-1) = 1 + 2T(n-1).
#              The first T(n-1) corresponds to the transfer of the n-1 rings from P1 to P2,
#              and the second T(n-1) corresponds to the transfer from P3 to P2. This recurrence solves to T(n) = 2^n - 1.
#              One way to see this is to "unwrap" the recurrence: T(n) = 1 + 2 + 4 + ... + 2^k T(n-k).
#              Printing a single move takes O(1) time, so the time complexity is O(2^n)


def tower_of_hanoi(fr, to, spare, n):
    res = []
    _tower_of_hanoi(n, fr, to, spare, res)
    return res


def _tower_of_hanoi(n, fr, to, spare, res):
    if n > 0:
        _tower_of_hanoi(n - 1, fr, spare, to, res)
        res.append([fr, to])
        _tower_of_hanoi(n - 1, spare, to, fr, res)


def tower_of_hanoi_2(fr, to, spare, n):
    res = []
    _tower_of_hanoi_2(n, fr, to, spare, res)
    return res


def _tower_of_hanoi_2(n, fr, to, spare, res):
    if n == 1:
        res.append([fr, to])
    else:
        _tower_of_hanoi_2(n - 1, fr, spare, to, res)
        _tower_of_hanoi_2(1, fr, to, spare, res)
        _tower_of_hanoi_2(n - 1, spare, to, fr, res)


if __name__ == "__main__":
    peg1, peg2, peg3 = 'fr', 'to', 'spare'
    print(tower_of_hanoi(peg1, peg2, peg3, 1))
    print(tower_of_hanoi(peg1, peg2, peg3, 2))
    print(tower_of_hanoi(peg1, peg2, peg3, 3))
    print(tower_of_hanoi(peg1, peg2, peg3, 4))

    print(tower_of_hanoi_2(peg1, peg2, peg3, 1))
    print(tower_of_hanoi_2(peg1, peg2, peg3, 2))
    print(tower_of_hanoi_2(peg1, peg2, peg3, 3))
    print(tower_of_hanoi_2(peg1, peg2, peg3, 4))