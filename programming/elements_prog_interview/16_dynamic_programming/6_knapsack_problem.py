"""
Write a program for the knapsack problem that selects a subset of items that has maximum value and satisfies the weight constraint.
All items have integer weights and values. Return the value of the subset.
"""


# Time = O(n w) where n is the number of items and w is the total allowed weight
# Space = O(n w)
def knapsack(items, weight):
    cache = [[-1 for _ in range(weight + 1)] for _ in items]
    cache, knapsack = _knapsack(items, weight, cache)
    print(cache)
    return knapsack


def _knapsack(items, weight, cache):
    if len(items) - 1 < 0:
        return cache, 0
    if cache[len(items) - 1][weight] == -1:
        cache, without_new_item = _knapsack(items[:-1], weight, cache)
        if weight < items[-1][1]:
            with_new_item = 0
        else:
            cache, with_new_item = _knapsack(items[:-1], weight - items[-1][1], cache)
            with_new_item += items[-1][0]
        cache[len(items) - 1][weight] = max(with_new_item, without_new_item)

    return cache, cache[len(items) - 1][weight]


if __name__ == "__main__":
    items = [[65, 20], [35, 8], [245, 60], [195, 55], [65, 40], [150, 70], [275, 85], [155, 25],
             [120, 30], [320, 65], [75, 75], [40, 10], [200, 95], [100, 50], [220, 40], [99, 10]]
    weight = 130
    print(knapsack(items, weight))

    items = [[60, 5], [50, 3], [70, 4], [30, 2]]
    weight = 5
    print(knapsack(items, weight))
