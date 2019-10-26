"""
Given a string containing a set of words separated by whitespace,
we would like to transform it to a string in which the words appear in the reverse order.
For example, "Alice likes Bob" transforms to "Bob likes Alice". We do not need to keep the original string
"""


# Time = O(n), Additional Space = O(n)
def reverse_sentence(s):
    ans = []
    beg = len(s) - 1
    end = len(s)

    while beg >= 0:
        while s[beg] != ' ' and beg >= 0:
            beg -= 1
        ans.append(s[beg + 1: end])
        end = beg + 1
        beg -= 1
    return ' '.join(ans)


if __name__ == '__main__':
    print(reverse_sentence('Alice likes Bob'))
