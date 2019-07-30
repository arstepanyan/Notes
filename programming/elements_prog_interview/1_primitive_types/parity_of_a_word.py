def parity(word):
    """
    Return 1 if the number of 1s in the word is odd. Otherwise, return 0
    :param word: binary word
    :return: 1 or 0
    >>> parity(11) # 1011
    1
    >>> parity(136) # 10001000
    0
    """
    bit_count = 0
    while word:
        bit_count += word & 1
        word >>= 1

    if bit_count % 2 == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()