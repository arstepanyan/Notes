"""
Write a program that takes text for an anonymous letter and text for a magazine and determines if it is possible to
write the anonymous letter using the magazine. The anonymous letter can be written using the magazine
if for each character in the anonymous letter, the number of times it appears in the anonymous letter
is no more than the number of times it appears in the magazine
"""


# Time = O(n + m) where n is the number of characters in the letter, m is the number of characters in the magazine
# Extra space = O(d) where d is the number of distinct characters in the letter
def anonymous_letter(l, m):
    char_counter = {}
    for c in l:
        if c == ' ':
            continue
        char_counter[c] = char_counter.get(c, 0) + 1

    for c in m:
        if c in char_counter:
            char_counter[c] -= 1
            if char_counter[c] == 0:
                del char_counter[c]
        if char_counter == {}:
            return True

    return False


if __name__ == "__main__":
    print(anonymous_letter('Python is great', 'Whoever uses Python enjoys its greatest convenience'))
    print(anonymous_letter('Python is great', 'Whoever uses Python enjoys it'))