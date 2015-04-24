# first occurrence


def find_first(arr, target):
    lo, high = 0, len(arr) - 1
    result = -1
    while lo <= high:
        mid = (lo + high) >> 1
        if arr[mid] == target:
            result = mid
            high = mid - 1
            print mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            high = mid - 1

    return result


if __name__ == "__main__":
    test_cases = [
        (([1, 1, 1, 1, 2, 3, 4, 5], 1), 0),
        (([4, 5], 1), -1),
        (([4, 5, 5], 5), 1),

    ]
    for test_case, exp in test_cases:
        print find_first(*test_case), exp



