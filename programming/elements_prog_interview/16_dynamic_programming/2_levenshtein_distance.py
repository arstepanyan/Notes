"""
Write a program that takes two strings and computes the minimum number of
edits needed to transform the first string into the second string.
"""


# Time = O(len(a) len(b))
#       Explanation: It takes O(1) to compute E(a[0: len(a) - 1], b[0: len(b) - 1])
#                    once E(a[0: k], b[0: l]) is known for all k < len(a), l < len(b)
# Space = O(len(word1) len(word2))
def distance_between_words(a, b):
    distances = [[-1 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
    return _distance_between_words(a, b, len(a) - 1, len(b) - 1, distances)


def _distance_between_words(a, b, idx1, idx2, distances):
    if idx1 < 0:
        # word1 is empty, so add all of word2's characters
        return idx2 + 1
    elif idx2 < 0:
        # word2 is empty, so delete all of word1's characters
        return idx1 + 1
    if distances[idx1][idx2] == -1:
        if a[idx1] == b[idx2]:
            distances[idx1][idx2] = _distance_between_words(a, b, idx1 - 1, idx2 - 1, distances)
        else:
            substitute_last = _distance_between_words(a, b, idx1 - 1, idx2 - 1, distances)
            add_last = _distance_between_words(a, b, idx1 - 1, idx2, distances)
            delete_last = _distance_between_words(a, b, idx1, idx2 - 1, distances)
            distances[idx1][idx2] = 1 + min(substitute_last, add_last, delete_last)
    return distances[idx1][idx2]


if __name__ == "__main__":
    print(distance_between_words('Saturday', 'Sundays'))
