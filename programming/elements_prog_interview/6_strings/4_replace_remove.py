"""
Write a program which takes as input an array of characters, and removes each 'b'
and replaces 'a' by two 'd's. Specifically, along with the array, you are provided an integer-valued size.
For example, if the array is <a, b, a, c, _> and the size is 4, then you can return <d, d, d, d, c>.
You can assume there is enough space in the array to hold the final result.
"""
def remove_replace(s, size):
    out_len = 0
    # Calculate the output length
    for el in s:
        if el == 'a':
            out_len += 2
        elif el != 'b' and el != '':
            out_len += 1
        else:
            continue

    # Remove, replace
    while size > 0:
        if s[size - 1] == 'a':
            s[out_len - 1], s[out_len - 2] = 'd', 'd'
            out_len -= 2
        elif s[size - 1] != 'b':
            s[out_len - 1] = s[size - 1]
            out_len -= 1
        size -= 1
    return s


if __name__ == '__main__':
    print(remove_replace(['a', 'b', 'a', 'c', ''], 4))
    print(remove_replace(['a', 'a', 'a', 'c', 'd', 'b', '', ''], 6))
