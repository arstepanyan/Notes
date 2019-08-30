'''
Write a program to test whether the letters forming a string can be permuted to form a palindrome.
For example, "edified" can be permuted to form "deified".
'''
import collections


def can_form_palindrom(s):
    '''
    Tests whether the letters forming the string s can be permuted to form a palindrome.
    :param s: string
    :return: True/False
    '''
    # A string can be permuted to form a palindrome if and only if the number of chars whose frequencies is odd at most 1.
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


if __name__ == '__main__':
    print(f'edified ... {can_form_palindrom("edified")}')
    print(f'abc ......  {can_form_palindrom("abc")}')
