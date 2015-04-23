# merge two sorted array


def merge(A, m, B, n):
    a, b, res = m - 1, n - 1, m + n - 1
    while a >= 0 or b >= 0:
        if a < 0 or A[a] < B[b]:
            A[res] = B[b]
            b -= 1
        elif b < 0 or A[a] >= B[b]:
            A[res] = A[a]
            a -= 1
        res -= 1

    return A


def merge2(A, m, B, n):
    a, b, res = m - 1, n - 1, m + n - 1
    while a >=0 and b >= 0:
        if A[a] >= B[b]:
            A[res] = A[a]
            a -= 1
        else:
            A[res] = B[b]
            b -= 1
        res -= 1

    while b >= 0:
        A[res] = B[b]
        res -= 1
        b -= 1
    return A



if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, None, None], 3, [1, 2], 2), [1, 1, 2, 2, 3]),
        (([2, 2, 2, None, None, None], 3, [1, 1, 1], 3), [1, 1, 1, 2, 2, 2]),
        # (([2, 2, 2], [3, 5]), []),
        # (([3, 4, 5], [2, 4]), [4])

    ]
    for (A, m, B, n), exp in test_cases:
        print merge2(A, m, B, n)