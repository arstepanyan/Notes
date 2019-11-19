"""
Write a program which takes as input an array and finds the distance between a closest pair of equal entries.
For example, if s = <"All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results">,
then the second and third occurrences of "no" is the closest pair.
"""

# Time = O(n)
# Extra Space = O(n)
def closest_dist(l):
    count_dict = {}
    for i, el in enumerate(l):
        if el in count_dict:
            count_dict[el].append(i)
        else:
            count_dict[el] = [i]

    min_dist = len(l)
    for word in count_dict:
        if len(count_dict[word]) == 1:
            continue
        cur_idx = 0
        for idx in count_dict[word][1:]:
            if idx - cur_idx < min_dist:
                min_dist = idx - cur_idx
            cur_idx = idx
    return None if min_dist == len(l) else min_dist


# Time = O(n)
# Extra Space = O(d) where d is the number of distinct entries in the array
def closest_dist_2(l):
    count_dict = {}
    min_dist = len(l)

    for i, el in enumerate(l):
        if el in count_dict:
            latest_index = count_dict[el]
            min_dist = min(min_dist, i - latest_index)
        count_dict[el] = i

    return None if min_dist == len(l) else min_dist



if __name__ == "__main__":
    print(closest_dist(["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]))
    print(closest_dist(['All', 'of', 'us']))

    print(closest_dist_2(["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]))
    print(closest_dist(['All', 'of', 'us']))
