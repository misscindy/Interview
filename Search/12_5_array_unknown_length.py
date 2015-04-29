

def search_arr_unknown_len(arr, target):

    def get(arr, ndx):
        try:
            return arr[ndx]
        except:
            return None

    lo, high = 0, 1
    while get(arr, high) and get(arr, high) < target:
        high <<= 1
    print high
    while lo <= high:
        mid = (lo + high) >> 1
        if not get(arr, mid) or get(arr, mid) > target:
            high = mid - 1
        elif get(arr, mid) == target:
            return mid
        else:
            lo = mid + 1
    return -1


if __name__ == "__main__":
    # For Question 1
    test_cases = [
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 3), (5, 6)),
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 7), 9),
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 9), 10),
        (([1, 1, 1, 1, 5], 5), 4),
        (([1], 1), 0),
    ]
    for test_case, expected in test_cases:
        print search_arr_unknown_len(test_case[0], test_case[1]), " == ", expected
        # print length(test_case[0], test_case[1]), " == ", len(test_case[0])
