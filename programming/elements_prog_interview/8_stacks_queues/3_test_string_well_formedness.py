"""
Write a program that tests if a string made up of the characters '(', ')', '[', ']', '{', and '}' is well-formed.

For example, '([]){()}' and '[()[]{()()}]' are well-formed, while '{)' and '[()[]{()()' are not well-formed.
"""


# Time = O(n)
# Space = O(n)
def well_formed(s, d):
    if not s:
        return False
    st = []
    for c in s:
        if c not in d:
            st.append(c)
        elif d[c] != st[-1]:
            return False
        else:
            st.pop()

    return st == []


if __name__ == "__main__":
    d = {')': '(', ']': '[', '}': '{'}
    s = '[()[]{()()}]'
    print(well_formed(s, d))

    s = '[()[]{()()'
    print(well_formed(s, d))

    s = '['
    print(well_formed(s, d))

    s = '[]'
    print(well_formed(s, d))

    s = ''
    print(well_formed(s, d))
