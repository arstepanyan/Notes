"""
Implement a routine that takes an n X m Boolean array A together with an entry (x, y)
and flips the color of the region associated with (x, y).

Define the region associated with (i, j) to be all points such that there exists a path from (i, j) to that point
in which all entries are the same color.
"""


# Time = O(|V| + |E|) same as DFS
def flip_color(array, loc):
    _flip_color(array, loc)
    return array


def _flip_color(array, loc):
    if not (0 <= loc[0] < len(array) and 0 <= loc[1] < len(array[0]) and array[loc[0]][loc[1]] == 'w'):
        return False

    array[loc[0]][loc[1]] = 'b'
    for i in [[loc[0] - 1, loc[1]], [loc[0] + 1, loc[1]], [loc[0], loc[1] - 1], [loc[0], loc[1] + 1]]:
        _flip_color(array, i)
    return True


# Time = O(mn), same as BFS
import collections


def flip_color_2(array, location):
    color = array[location[0]][location[1]]
    array[location[0]][location[1]] = 1 - array[location[0]][location[1]]  # flips the color
    q = collections.deque([location])

    while q:
        loc = q.popleft()
        for i in [[loc[0] - 1, loc[1]], [loc[0] + 1, loc[1]], [loc[0], loc[1] - 1], [loc[0], loc[1] + 1]]:
            if 0 <= i[0] < len(array) and 0 <= i[1] < len(array[0]) and array[i[0]][i[1]] == color:
                array[i[0]][i[1]] = 1 - array[i[0]][i[1]]  # Flip the color
                q.append(i)
    return array


if __name__ == "__main__":
    array = [['w', 'b', 'w', 'b'],
             ['w', 'w', 'b', 'w'],
             ['w', 'w', 'w', 'b'],
             ['b', 'w', 'w', 'b']]
    print(flip_color(array, [2, 2]))

    array = [[0, 1, 0, 1],
             [0, 0, 1, 0],
             [0, 0, 0, 1],
             [1, 0, 0, 1]]
    print(flip_color_2(array, (2, 2)))
