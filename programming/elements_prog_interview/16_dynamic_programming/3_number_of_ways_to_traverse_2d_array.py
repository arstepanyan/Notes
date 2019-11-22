"""
Write a program that counts how many ways you can go from the top-left to the bottom-right in a 2D array.
All moves must either go right or down.
"""


# Time = O(nm) where n is the number of rows and m is the number of columns
# Space = O(nm)
def num_ways(n, m):
    cache = [[0 for _ in range(m)] for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if row == 0 or col == 0:
                cache[row][col] = 1
            else:
                cache[row][col] = cache[row - 1][col] + cache[row][col - 1]
    return cache[-1][-1]


if __name__ == "__main__":
    print(num_ways(5, 5))
