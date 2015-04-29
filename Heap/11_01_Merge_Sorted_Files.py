from heapq import *
from heapq_showtree import show_tree


def merge_sorted_file(ls_of_filedata):
    min_heap = []
    # (heap : (value, origin))
    result = []
    for origin, cur_file in enumerate(ls_of_filedata):
        if cur_file:
            heappush(min_heap, (cur_file[0], origin, 1))

    while min_heap:
        nxt_min, origin, nxt_ndx = heappop(min_heap)
        result.append(nxt_min)
        nxt_file = ls_of_filedata[origin]
        if nxt_ndx < len(nxt_file):
            heappush(min_heap, (nxt_file[nxt_ndx], origin, nxt_ndx + 1))
    return result

    return min_heap

if __name__ == '__main__':
    test_cases = [
        ([[1, 2], [2, 3, 4, 5]], [1, 2, 2, 3, 4, 5]),
        ([[1, 2], [2, 3, 4, 5], [3, 4, 5]], [1, 2, 2, 3, 3, 4, 4, 5, 5]),

    ]
    for test_case, exp in test_cases:
        show_tree(merge_sorted_file(test_case))
        print(merge_sorted_file(test_case)) == exp






