# Merge Sort
# Quick Sort
# Selection
# Counting Sort
# Radix Sort
# Heap Sort file: Heap_Review


def merge_sort(a):
    _merge_sort(a, a[:], 0, len(a) - 1)


def _merge_sort(a, aux, lo, high):
    # print "_merge_sort", a, aux, lo, high
    if lo >= high:
        return
    mid = (lo + high) >> 1

    _merge_sort(a, aux, lo, mid)
    _merge_sort(a, aux, mid + 1, high)
    _merge(a, aux, lo, mid + 1, high)


def _merge(a, aux, lo, mid, high):
    # print "_merge: ", a, aux, lo, mid, high
    aux[lo: high + 1] = a[lo: high + 1]

    left, right, nxt = lo, mid, lo
    while left < mid or right <= high:
        if left >= mid:
            a[nxt] = aux[right]
            right += 1
        elif right > high:
            a[nxt] = aux[left]
            left += 1
        elif aux[left] >= aux[right]:
            a[nxt] = aux[right]
            right += 1
        else:
            a[nxt] = aux[left]
            left += 1
        nxt += 1

import random
# Partition


def partition(a, lo, high):
    # randomly pick a pivot
    if lo > high:
        return
    # print lo, high
    pivot_ndx = random.randint(lo, high)
    a[lo], a[pivot_ndx] = a[pivot_ndx], a[lo]
    # pick random pivot
    pivot_ndx, pivot = lo, a[lo]
    i, j = lo + 1, high
    # print "pivot", pivot
    while True:
        while i < high and a[i] < pivot:
            i += 1
        while j > lo and a[j] > pivot:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]

    a[pivot_ndx], a[j] = a[j], a[pivot_ndx]
    return j


class IndexOutOfBounds(Exception):
    pass


def quick_select(a, k):
    if k < 0 or k >= len(a):
        raise IndexOutOfBounds("invalid parameter")
    lo, high = 0, len(a) - 1
    while lo < high:
        pivot_ndx = partition(a, lo, high)
        if pivot_ndx > k:
            pivot_ndx = partition(a, lo, pivot_ndx - 1)
        elif pivot_ndx < k:
            pivot_ndx = partition(a, pivot_ndx + 1, high)
        else:
            return pivot_ndx, a[pivot_ndx]
    return lo, a[lo]


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 3], sorted([3, 2, 1, 3])),
        # ([3, 2, 5, 4, 3, -2, 1], sorted([3, 2, 5, 4, 3, -2, 1])),

        # ([1, -2, -5], sorted([1, -2, -5])),
        ([1], sorted([])),

        # ([1], sorted([1])),
        ]
    for test_case, exp in test_cases:
        ########Mergesort test_case
        # merge_sort(test_case)
        # print test_case == exp
        ########Quickselect test_case
        print test_case
        # print quick_select(test_case, 3)
        print quick_select(test_case, 0)






