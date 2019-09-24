# Write a program that takes a set of events, and determines the maximum number of events that take place concurrently.

# O(n log n) time complexity ([create a new list = O(n)] + [sort = O(n log n)] + [iterate through each endpoint = O(n)])
# O(n) extra space complexity for the endpoints
def concurrent_events(events):
    """
    Computes the maximum number of concurrent events
    :param events: List[List[int]]
    :return: int
    """
    endpoints = [t for event in events for t in [(event[0], True), (event[1], False)]]
    endpoints.sort()

    max = 0
    cur_max = 0
    for endpoint in endpoints:
        if endpoint[1] is True:
            cur_max += 1
        else:
            cur_max -= 1
        if cur_max > max:
            max = cur_max
    return max


if __name__ == "__main__":
    events = [[1, 5], [2, 7], [4, 5], [6, 10], [8, 9], [9, 17], [11, 13], [12, 15], [14, 15]]
    print(concurrent_events(events))

