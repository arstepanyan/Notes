import functools
import string

def int_to_string(num):
    """
    Convert int to string without using builtin str()
    :param num: integer
    :return: string representation of the given integer
    >>> int_to_string(124)
    '124'
    """
    if num < 0:
        num, is_neg = -num, True
    else:
        is_neg = False

    s = []
    while num > 0:
        s.append(chr(ord('0') + num%10))
        num //= 10

    return ('-' if is_neg else '') + ''.join(reversed(s))


def string_to_int(s):
    """
    Convert string to int
    :param s: string
    :return: integer representation of the string
    >>> string_to_int('123')
    123
    """
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c),
                            s[s[0] == '-':], 0) * (-1 if s[0] == '' else 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    num = 124
    s = '123'
    print(f'int_to_string(124) ...... {int_to_string(num)}')
    print(f'string_to_int("123") .... {string_to_int(s)}')