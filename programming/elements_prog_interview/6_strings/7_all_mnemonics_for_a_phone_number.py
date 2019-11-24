"""
Write a program which takes as input a phone number, specified as a string of digits,
and returns all possible character sequences that correspond to the phone number.
The cell phone keypad is specified by a mapping that takes a digit and returns the corresponding set of characters.
The character sequences do not have to be legal words or phrases.
"""


# Time = O(n 4^n) Explanation: Since there are no more than 4 possible characters for each digit,
#                              the number of recursive calls, T(n), satisfies T(n) <= 4 T(n-1), where n is the number
#                              of digits in the number. This solves to T(n) = O(4^2).
#                              For the function calls that entail recursion, the time spent within the function,
#                              not including the recursive calls, is O(1).
#                              Each base case entails making a copy of a string and adding it to the result.
#                              Since each such string has length n, each base case takes time O(n).
#                              Therefore, the time complexity is O(n 4^n)
def find_mnemonics(number, digit_to_char):
    res = []
    _find_mnemonics(number, digit_to_char, res, [])
    return res


def _find_mnemonics(number, digit_to_char, res, buf):
    if len(number) == 0:
        res.append(''.join(buf))
    else:
        for char in digit_to_char[int(number[0])]:
            buf.append(char)
            _find_mnemonics(number[1:], digit_to_char, res, buf)
            buf.pop()


if __name__ == "__main__":
    digit_to_char = {0: [], 1: [], 2: ["A", "B", "C"],
                     3: ["D", "E", "F"], 4: ["G", "H", "I"],
                     5: ["J", "K", "L"], 6: ["M", "N", "O"],
                     7: ['P', "Q", "R", "S"], 8: ["T", "U", "V"],
                     9: ["W", "X", 'Y', "Z"]}

    print(find_mnemonics('276', digit_to_char))
