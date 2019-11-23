"""
Write a program that makes a single pass over the sequence and identifies the majority element.
You know a priori that more than half the strings are repetitions of a single string but the positions where the majority element occurs are unknown.
For example, if the input is ['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a'], then 'a' is the majority element (it appears in 6 out of the 10 places).
"""


# Time = O(n)
# Space = O(1)
# Explanation of the solution: The algorithm is as follows. We have a candidate for the majority element, and track its count.
#                              It is initialized to the first entry. We iterate through remaining entries.
#                              Each time we see an entry equal to the candidate, we increment the count.
#                              If the entry is different, we decrement the count.
#                              If the count becomes zero, we set the next entry to be the candidate.
#                              Mathematically, Let's say the majority element occured m times out of n entries.
#                              By definition m/n > 1/2. At most one of the two distinct entries that are discarded can be the majority element.
#                              Hence, after discarding them, the ratio of the number of remaining majority elements
#                              to the total number of remaining elements is either m/(n-2) (neither discarded elements was majority element)
#                              or (m-1)/(m-2) (one of the discarded element was majority element). Both are greater than 1/2.


# Time = O(n)
# Space = O(1)
def majority_element(array):
    candidate, candidate_count = array[0], 1
    for el in array[1:]:
        if candidate_count == 0:
            candidate = el
        if el == candidate:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate


if __name__ == "__main__":
    print(majority_element(['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a']))
