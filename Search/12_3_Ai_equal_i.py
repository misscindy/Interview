# find the A[i] = i, A sorted and distinct
#  -> A[i] >= A[i - 1] + 1
#  -> A[i] - i >= A[i - 1] + 1 - (i - 1)


def search_fix_pt(arr):
    lo, high = 0, len(arr) - 1
    while lo <= high:
        mid = (lo + high) >> 1
        v = arr[mid] - mid
        if v == 0:
            return mid
        elif v < 0:
            lo = mid + 1
        else:
            high = mid - 1
    return -1


def _search(arr, lo, high):
    if lo > high:
        return -1
    mid = (lo + high) >> 1
    v = arr[mid] - mid
    if v == 0:
        return mid
    elif v < 0:
        return _search(arr, mid + 1, high)
    else:
        return _search(arr, lo, mid - 1)

if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2, 3, 4, 5], (1, 2, 3, 4, 5)),
        ([4, 5], (-1,)),


    ]
    for test_case, exp in test_cases:
        print search_fix_pt(test_case) in exp
        print _search(test_case, 0, len(test_case)) in exp
