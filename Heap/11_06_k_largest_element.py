import random


def partition(a, lo, high):
    if lo == high:
        return lo
    pivot_ndx = random.randint(lo, high)
    print lo, high, pivot_ndx
    a[lo], a[pivot_ndx] = a[pivot_ndx], a[lo]
    pivot = a[lo]
    i, j = lo + 1, high
    while i < j:
        while i < high and a[i] < pivot:
            i += 1
        while j > lo and a[j] > pivot:
            j -= 1

        if i >= j:
            break
        a[j], a[i] = a[i], a[j]
    a[j], a[lo] = a[lo], a[j]
    return j



if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 3], sorted([3, 2, 1, 3])),
        # ([3, 2, 5, 4, 3, -2, 1], sorted([3, 2, 5, 4, 3, -2, 1])),

        # ([1, -2, -5], sorted([1, -2, -5])),
        # ([1], sorted([1])),

        # ([1], sorted([1])),
        ]
    for test_case, exp in test_cases:

        print test_case
        print partition(test_case, 0, 3)
        print test_case
        # print quick_select(test_case, 0)

