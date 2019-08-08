# O(2^n) solution
def pow(x, y):
    """
    Computes x to the power of y
    :param x: float
    :param y: nonnegative integer
    :return: x to the power of y
    >>> pow(2, 3)
    8
    """
    result = x
    for i in range(y-1):
        result *= x
    return result

# With recursion
def pow2(x, y):
    """
    >>> pow(2, 4)
    16
    """
    if y == 1:
        return x
    return x * pow(x, y-1)

# O(n) solution with binary representation of y, as well as properties of exponentiation, specifically x^(y0+y1) = x^y0 * x^y1
# For example, x^1010 = x^(101 + 101) = x^101 * x^101
# Similarly,   x^101 = x^(100 + 1) = x^100 * x = x(10) * x^10 * x
# Generalizing, if the least significant bit of y is 0, the results is (x^(y/2))^2; otherwise, it is x * (x^(y/2))^2
# When y is negative, x is replaced by 1/x and y by -y
def pow3(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()