repr_dict = {10: 'A',
             11: 'B',
             12: 'C',
             13: 'D',
             14: 'E',
             15: 'F'}


def base_conversion(s, b1, b2):
    def b1_to_int(string, base):
        if len(string) == 1:
            return int(string[0])
        return int(string[0]) * base ** (len(string) - 1) + b1_to_int(string[1:], base)

    is_negative = s[0] == '-'
    integer = b1_to_int(s[is_negative:], b1)
    ans = []
    while True:
        ans.append(repr_dict.get(integer % b2, chr(ord('0') + integer % b2)))
        integer //= b2
        if integer == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(ans))


if __name__ == "__main__":
    print(base_conversion('615', 7, 13))
