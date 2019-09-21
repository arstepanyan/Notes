# Write a program which takes a nonnegative integer
# and returns the largest integer whose square is less than or equal to the given integer.
# For example, if the input is 16, return 4; if the input is 300, return 17, since 17^2 = 289 < 300 and 18^2 = 324 > 300.
def largest_sqrt(k):
    """
    Return largest integer whose square is less than or equal to k
    :param k: int, nonnegative
    :return: largest integer whose square is less than or equal to k
    """
    last_num = 1
    while last_num * last_num < last_num:
        last_num *= 2
    last_num /= last_num
    while last_num * last_num <= k:
        last_num += 1
    return last_num - 1


# Faster
def largest_sqrt2(k):
    """
    Return largest integer whose square is less than or equal to k
    :param k: int, nonnegative
    :return: largest integer whose square is less than or equal to k
    """
    last_num = 1
    while last_num * last_num < last_num:
        last_num *= 2
    last_num /= last_num
    left, right = last_num, k
    while left <= right:
        middle = (left + right) // 2
        if middle * middle <= k:
            left = middle + 1
        else:
            right = middle - 1
    return left - 1


# Fastest
def square_root(k):
    """
        Return largest integer whose square is less than or equal to k
        :param k: int, nonnegative
        :return: largest integer whose square is less than or equal to k
        """
    left, right = 0, k
    while left <= right:
        middle = (left + right) // 2
        if middle * middle <= k:
            left = middle + 1
        else:
            right = middle - 1
    return left - 1


if __name__ == "__main__":
    import time

    t0 = time.time()
    print('largest_sqrt', largest_sqrt(300))
    print(f'\t\t {round(time.time() - t0, 10)} seconds')

    t0 = time.time()
    print('largest_sqrt2()', largest_sqrt2(300))
    print(f'\t\t {round(time.time() - t0, 10)} seconds')

    t0 = time.time()
    print('square_root()', square_root(300))
    print(f'\t\t {round(time.time() - t0, 10)} seconds')
