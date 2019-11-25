"""
Given a dictionary D and two strings s and t, write a program to determine if s produces t.
Assume that all characters are lowercase alphabets. If s does produce t, output
the length of the shortest production sequence; otherwise, output -1.

Define s to produce t if there exists a sequence of strings from the dictionary P = {s0, s1, ..., sn}
such that the first string is s, the last string is t, and adjacent strings have the same length and differ
in exactly one character. The sequence P is called a production sequence.

For example, if the dictionary is {"bat", "cot", "dog", "dat", "dot", "cat"},
then ["cat", "cot", "dot", "dog"] is production sequence.
"""

import collections
import string


# Time = O(d^2), where d is the number of vertices (it is the same as the number of words in the dictionary).
#                Explanation: The number of edges is O(d^2) in the worst case => time complexity is the same as BFS
#                which is O(d + d^2) = O(d^2)
#                If the string length is less than d then the maximum number of edges out of the vertex is O(n),
#                implying an O(nd) bound.
def find_seq(D, s, t):
    q = collections.deque([[s, 0]])
    D.remove(s)

    while q:
        cur = q.popleft()
        if cur[0] == t:
            return cur[1]

        # Tries all possible transformations of cur
        for i in range(len(cur[0])):
            for c in string.ascii_lowercase:  # Iterates through a-z
                candidate = cur[0][:i] + c + cur[0][i + 1:]
                if candidate in D:
                    D.remove(candidate)
                    q.append([candidate, cur[1] + 1])
    return -1


if __name__ == "__main__":
    D = {"bat", "cot", "dog", "dag", "dot", "cat"}
    s, t = "cat", "dog"
    print(find_seq(D, s, t))

    D = {"bat", "cot", "dog", "dag", "dom", "cat"}
    s, t = "cat", "dog"
    print(find_seq(D, s, t))
