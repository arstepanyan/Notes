"""
Consider a black and white idgital image of maze - white pixels represent open areas and black spaces are walls.
There are two special white pixels; one is designates the entrance and the other is the exit.
The goal in this problem is to find a way of getting from the entrance to the exit.

Given a 2D array of black and white entries representing a maze with designated entrance and exit points,
find a path from the entrance to the exit, if one exists.
"""


# Time = O(|V| + |E|) which is the same as for the DFS
# Space = O(1)
def search_maze(array):
    return _search_maze(array, [len(array) - 1, 0])


def _search_maze(array, loc):
    if array[loc[0]][loc[1]] == 'E':
        return True

    array[loc[0]][loc[1]] = 'v'
    for i in [[loc[0] + 1, loc[1]], [loc[0], loc[1] + 1], [loc[0] - 1, loc[1]], [loc[0], loc[1] - 1]]:
        if (0 <= i[0] < len(array)) and (0 <= i[1] < len(array[0])):
            if array[i[0]][i[1]] != 'b' and array[i[0]][i[1]] != 'v':
                if _search_maze(array, i):
                    return True
    return False


if __name__ == "__main__":
    array = [['w', 'w', 'w', 'w', 'E'],
             ['w', 'b', 'w', 'b', 'w'],
             ['w', 'b', 'w', 'w', 'w'],
             ['S', 'w', 'w', 'b', 'b']
             ]
    print(search_maze(array))

    array = [['w', 'w', 'w', 'w', 'E'],
             ['w', 'b', 'b', 'b', 'b'],
             ['w', 'w', 'w', 'w', 'w'],
             ['w', 'b', 'w', 'w', 'w'],
             ['S', 'w', 'w', 'b', 'b']]
    print(search_maze(array))

    array = [['w', 'w', 'w', 'b', 'E'],
             ['w', 'b', 'b', 'b', 'b'],
             ['w', 'w', 'w', 'w', 'w'],
             ['S', 'w', 'w', 'b', 'b']]
    print(search_maze(array))
