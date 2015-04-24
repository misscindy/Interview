# Binary Search
# In sorted array
# Selection Search
# In unordered array


def b_search_i(a, target):
    lo, high = 0, len(a) - 1
    while lo <= high:
        mid = (lo + high) >> 1
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            lo = mid + 1
        else: # a[mid] > target
            high = mid - 1

    return -1


def b_search_r(a, target):

    def _search(a, target, lo, high):
        if lo > high:
            return -1
        mid = (lo + high) >> 1
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            return _search(a, target, mid + 1, high)
        else:
            return _search(a, target, lo, mid - 1)

    start, end = 0, len(a) - 1
    return _search(a, target, start, end)

# def selection()
import random

# test_case [2, 3, 1, 4]


def partition(a, lo, high):
    if lo >= high:
        return
    pivot_ndx = random.randint(lo, high)
    pivot = a[pivot_ndx]
    a[lo], a[pivot_ndx] = a[pivot_ndx], a[lo]
    pivot, pivot_ndx = a[lo], lo
    i, j = lo + 1, high
    while True:
        while i < high and a[i] < pivot:
            i += 1
        while j > lo and a[j] > pivot:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[j], a[pivot_ndx] = a[pivot_ndx], a[j]
    return j


if __name__ == "__main__":
    test_cases = [
        (([1, 1, 2, 3, 4, 5], 1), (0, 1)),
        (([4, 5], 1), (-1,)),
        (([4, 5], 5), (1,)),

    ]
    for test_case, exp in test_cases:
        print b_search_i(*test_case) in exp
        print b_search_r(*test_case) in exp
