# Brute force O(n^2) time complexity, additional space O(1)
def buy_sell_stock1(a):
    """
    Given an array denoting the daily stock price,
    return the maximum profit that could be made
    by buying and then selling one share of that stock.
    :param a: list
    :return: integer
    >>> buy_sell_stock1([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
    30
    """
    result = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] - a[i] > result:
                result = a[j] - a[i]
    return result

# Time complexity = O(n), additional space = O(n)
def buy_sell_stock2(a):
    # Create a new list of the same size. ith element of the new list is the maximum of the a[i:]
    maxs = [a[-1]]
    for i in reversed(range(1, len(a))):
        if a[i] >= maxs[-1]:
            maxs.append(a[i])
        else:
            maxs.append(maxs[-1])

    # Compute the differences between the ith element of the the list and the (-1-i)th element of the original array.
    # The maximum difference is our answer
    res = 0
    for i in range(len(maxs)):
        if maxs[i] - a[-1-i] > res:
            res = maxs[i] - a[-1-i]
    return res

# Time complexity = O(n), space complexity = O(1). Modified buy_sell_stock2
def buy_sell_stock3(a):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in a:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(buy_sell_stock1([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
    print(buy_sell_stock2([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
    print(buy_sell_stock3([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
