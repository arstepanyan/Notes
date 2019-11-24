"""
Write a program that takes as input an integer n and returns the n th integer in the look-and-say sequence.
Return the result as a string.

The look-and-say sequence starts with 1. Subsequent numbers are derived by describing the previous number in terms of consecutive digits.
Specifically, to generate an entry of the sequence from the previous entry, read off the digits of the previous entry,
counting the number of digits in groups of the same digit.

For example, 1; one 1; two 1s; one 2 then one 1; one 1, then one 2, then two 1s; three 1s, then two 2s, then one 1.
The first eight numbers in the look-and-say sequence are [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211].
"""


# Time = bound O(n 2^n)
# Explanation: Each successive number can have at most twice as many digits as the previous number
#              - this happens when all digits are different. This means the maximum length number has length no more than 2^n.
#              Since there are n iterations and the work in each iteration is proportional to the length of the number
#              computed in the iteration, a simple bound on the time complexity is O(n 2^n).
def look_and_say(n):
    cur = '1'
    for _ in range(n - 1):
        cur = _look_and_say(cur)
    return cur


def _look_and_say(num):
    prev, count, res = num[0], 0, []
    i = 0
    while i < len(num):
        if num[i] == prev:
            count += 1
        else:
            res.append(str(count))
            res.append(prev)
            prev, count = num[i], 1
        i += 1
    res.append(str(count))
    res.append(prev)
    return ''.join(res)


if __name__ == "__main__":
    print(look_and_say(2))
    print(look_and_say(5))
