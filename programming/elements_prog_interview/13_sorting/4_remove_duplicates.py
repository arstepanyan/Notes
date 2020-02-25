"""
Design an efficient algorithm for removing all first-name duplicates from an array.
For example, if the input is <(Ian,Bothan), (David,Gower), (Ian,Bell), (Ian,Chappell)>,
one result could be <((Ian,Bothan), (David,Gower)>; <(David,Gower), (Ian,Bell)> would also be acceptable.
"""

# Could be done in O(n) time using extra O(n) space for a hash table

# Time complexity = O(n log n)  (O(n log n) to sort and O(n) to eliminate duplicates)
# Extra space complexity = O(1) (We are reusing the input array to store the results)
def remove_duplicates(names):
    names.sort(key = lambda x: x[0])
    write_index = 1
    for i in range(1, len(names)):
        if names[i][0] != names[i - 1][0]:
            names[write_index] = names[i]
            write_index += 1
    return names[:write_index]


if __name__ == '__main__':
    names = [['james', 'smith'], ['ann', 'taylor'], ['ann', 'morgan'], ['john', 'kurkman'], ['james', 'blunt']]
    print(remove_duplicates(names))
