# Write a program that takes an n X n 2D array and returns the spiral ordering of the array
def spiral_matrix(M):
    first_row, last_row = 0, len(M) - 1
    first_col, last_col = 0, len(M[0]) - 1
    res = []

    while first_col <= last_col:
        if first_col <= last_col:
            for row_el in range(first_col, last_col + 1):
                res.append(M[first_row][row_el])
        first_row += 1

        if first_row <= last_row:
            for col_el in range(first_row, last_row + 1):
                res.append(M[col_el][last_col])
        last_col -= 1

        for row_el in reversed(range(first_col, last_col + 1)):
            res.append(M[last_row][row_el])
        last_row -= 1

        for col_el in reversed(range(first_row, last_row + 1)):
            res.append(M[col_el][first_col])
        first_col += 1

    return res

if __name__ == "__main__":
    M1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    M2 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
    M3 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]
    print(spiral_matrix(M1))
    print(spiral_matrix(M2))
    print(spiral_matrix(M3))