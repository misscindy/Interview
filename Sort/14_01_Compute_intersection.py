# Give A, B sorted array
# Return C with common elements without duplicates


# when n, m are comparable in size
# two pointers move simultaneously
def intersect(A, B):
    res = []
    a_iter, b_iter = 0, 0
    while a_iter < len(A) and a_iter < len(B):
        # if ((a_iter != 0 and A[a_iter] == A[a_iter - 1])
        #         or (A[a_iter] < B[b_iter])):
        #     a_iter += 1
        # elif ((b_iter != 0 and B[b_iter] == B[b_iter - 1])
        #         or (A[a_iter] > B[b_iter])):
        #     b_iter += 1
        #
        # else:
        #     # print a_iter, b_iter
        #     res.append(A[a_iter])
        #     a_iter, b_iter = a_iter + 1, b_iter + 1
        if A[a_iter] == B[b_iter] and (a_iter == 0 or A[a_iter] != A[a_iter - 1]):
            res.append(A[a_iter])
            a_iter, b_iter = a_iter + 1, b_iter + 1
        elif A[a_iter] > B[b_iter]:
            b_iter += 1
        else:
            a_iter += 1

    return res


# when n << m


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], [1, 2]), [1, 2]),
        (([1, 2, 2], [1, 2, 5]), [1, 2]),
        (([2, 2, 2], [3, 5]), []),
        (([3, 4, 5], [2, 4]), [4])

    ]
    for (A, B), exp in test_cases:
        print intersect(A, B)