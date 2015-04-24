

def first_greater(arr, target):
    # [1, 2, 3, 5]
    lo, high = 0, len(arr) - 1
    result = -1
    while lo <= high:
        mid = (lo + high) >> 1
        if arr[mid] > target:
            result = mid
            high = mid - 1
        else:
            lo = mid + 1
    return result

# def find_first_greater(arr, target:
#     lo, high = 0, len(arr) - 1
#     while lo <= high:
#         mid = (lo + high >> 1
#         if arr[mid]

if __name__ == "__main__":
    test_cases = [
        (([1, 1, 2, 3, 4, 5], 1), 2),
        (([4, 5], 1), 0),
        (([4, 5], 5), -1),

    ]
    for test_case, exp in test_cases:
        print first_greater(*test_case), exp

