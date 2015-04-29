# compute integer sqrt
# [1, 4, 9, 16, 25, ...]


def int_sqrt(n):
    lo, high = 0, n
    if n < 0:
        return -1
    while lo <= high:
        mid = (lo + high) >> 1
        mid_val = mid * mid
        if mid_val <= n < (mid + 1) * (mid + 1):
            return mid
        elif mid_val > n:
            high = mid - 1
        else:
            lo = mid + 1
    return -1


if __name__ == "__main__":
    # For Question 1
    test_cases = [
        (1, 1),
        (2, 1),
        (6, 2),
        (0, 0),
    ]
    for test_case, expected in test_cases:
        print int_sqrt(test_case) == expected
        # print length(test_case[0], test_case[1]), " == ", len(test_case[0])
