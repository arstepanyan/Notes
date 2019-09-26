# Write a program which takes and integer
# and returns the integer corresponding to the digits of the input written in reverse order.
# For example, the reverse of 42 is 24, and the reverse of -314 is -413

# Time complexity is O(n), where n is the number of digits in num
# Additional Space complexity is O(n) too
def reverse_digits1(num):
    res = []
    if num < 0:
        res.append('-')
        num = abs(num)
    elif num == 0:
        return 0

    while num:
        if num < 10:
            res.append(str(num))
        else:
            res.append(str(num % 10))
        num //= 10
    return int(''.join(res))

# Time complexity O(n), where n is the number of digits in num
# Additional space complexity is O(1)
def reverse_digits2(num):
    res, remainder = 0, abs(num)
    while remainder:
        res = res * 10 + remainder % 10
        remainder //= 10
    return -res if num < 0 else res


if __name__ == "__main__":
    print(reverse_digits1(42))
    print(reverse_digits1(-314))
    print(reverse_digits1(0))
    print(reverse_digits2(-42))
    print(reverse_digits2(10))

