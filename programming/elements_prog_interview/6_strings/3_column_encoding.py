import functools

def encode(col_name):
    """
    Compute column encoding given "A"->1, "B" -> 2, "AA" -> 27, "ZZA" -> 18253
    :param col_name: string, for example "A", "BA", "ZZH", etc
    :return: integer
    >>> encode("A")
    1
    >>> encode("Z")
    26
    >>> encode("ZA")
    677
    >>> encode("ZZZ")
    18278
    """
    return functools.reduce(lambda res, c: res*26 + ord(c) - ord('A') + 1, col_name, 0)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(f'encode("ZA") ...... {encode("ZA")}')