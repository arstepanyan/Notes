'''
Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence.
For example, if the input is [3, 5, 7], [0, 6], and [0, 6, 28], then the output is [0, 0, 3, 5, 6, 6, 7, 28].
'''
import heapq

def merge_sorted_arrays(sorted_lists):
    min_heap = []
    iters = [iter(x) for x in sorted_lists]

    for i, el in enumerate(iters):
        next_el = next(el, None)
        if next_el is not None:
            heapq.heappush(min_heap, [next_el, i])

    result = []

    while min_heap:
        min_element, min_element_i = heapq.heappop(min_heap)
        result.append(min_element)
        next_el = next(iters[min_element_i], None)
        if next_el is not None:
            heapq.heappush(min_heap, [next_el, min_element_i])

    return result

if __name__ == '__main__':
    list1 = [1, 4, 5]
    list2 = [2, 3, 6, 20]
    list3 = [1, 2]

    print(f'list1 ....... {list1}')
    print(f'list1 ....... {list2}')
    print(f'list1 ....... {list3}')

    merged_lists = merge_sorted_arrays(sorted_lists = [list1, list2, list3])
    print(f'merged .......... {merged_lists}')