"""
In an American football game, a play can lead to 2 points (safety), 3 points (field goal), or 7 points (touchdown, assuming the extra point).
Many different combinations of 2, 3, and 7 point plays can make up a final score. For example, four combinations of plays yield a score of 12.

* 6 safeties (2 X 6 = 12),
* 3 safeties and 2 field goals (2 X 3 + 3 X 2 = 12),
* 1 safety, 1 field goal and 1 touchdown (2 X 1 + 3 X 1 + 7 X 1 = 12).
* 4 field goals (3 X 4 = 12).

Write a program that takes a final score and scores for individual plays,
and returns the number of combinations of plays that result in the final score
"""


# Time = O(n target) where n is the number of elements in the nums list
# Space = O(n target) to store the 2D array
def combs_sum(nums, target):
    cache = [[0 for _ in range(target + 1)] for _ in nums]

    for row, num in enumerate(nums):
        for col in range(target + 1):
            if row == 0:
                cache[row][col] = 1 if col % num == 0 else 0
            elif col < num:
                cache[row][col] = cache[row - 1][col]
            else:
                cache[row][col] = cache[row - 1][col] + cache[row][col - num]
    return cache[- 1][-1]


if __name__ == "__main__":
    # The 2D cache of nums = [2, 3, 4] and target = 12 is
    # [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    # [1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3]
    # [1, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
    print(combs_sum([2, 3, 7], 12))
