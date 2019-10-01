# Check whether a 9 X 9 2D array representing a partially completed Sudoku is valid.
# Specifically, check that no row, column or 3 X 3 2D subarray contains duplicates.
# A 0-value in the 2D array indicates that entry is blank; every pther entry is in [1, 9].

def sudoku_chekcer(M):
    # Check the rows
    for row in M:
        cur_counter = set()
        for el in row:
            if el in cur_counter:
                return False
            elif el != 0:
                cur_counter.add(el)

    # Check the columns
    for col in range(len(M[0])):
        cur_counter = set()
        for row in range(len(M)):
            if M[row][col] in cur_counter:
                return False
            elif M[row][col] != 0:
                cur_counter.add(M[row][col])

    # Check the 2D subarrays
    for row_jumper in range(0, len(M[0]), 3):
        for col_jumper in range(0, len(M), 3):
            cur_counter = set()
            for i in range(3):
                for j in range(3):
                    if M[row_jumper + i][col_jumper + j] in cur_counter:
                        return False
                    elif M[row_jumper + i][col_jumper + j] != 0:
                        cur_counter.add(M[row_jumper + i][col_jumper + j])
    return True




if __name__ == "__main__":
    M1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
         ]
    M2 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 8, 8, 0, 0, 7, 9]
        ]

    print(sudoku_chekcer(M1))
    print(sudoku_chekcer(M2))

