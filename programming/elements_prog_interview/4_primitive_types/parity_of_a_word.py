# parity1 and parity2 - Time complexity is O(n) where n is the word size
def parity1(x):
    """
    Return 1 if the number of 1s in the word is odd. Otherwise, return 0
    :param word: binary word
    :return: 1 or 0
    >>> parity1(11) # 1011
    1
    >>> parity1(136) # 10001000
    0
    """
    bit_count = 0
    while x:
        bit_count += x & 1
        x >>= 1
    if bit_count % 2 == 0:
        return 0
    else:
        return 1
# nicer
def parity2(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

# parity3 - time complexity is k where k is the number of 1s
def parity3(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1  # Drops the lowest set bit of x
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(f'parity2(11) ... {parity2(11)}')
    print(f'parity3(11) ... {parity2(11)}')





