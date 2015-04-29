# Find the longest common sub sequence of two strings


def lcs_memo(a, b):
    look_up = dict()
    return _lcs(a, b, look_up)


def _lcs(a, b, lookup):
    if (a, b) in lookup:
        # print "look_up : _lcs(%s, %s)" % (a, b)
        return lookup[(a, b)]
    # print "_lcs(%s, %s)" % (a, b)
    if len(a) == 0 or len(b) == 0:
        lookup[(a, b)] = [0, ""]
        return 0, ""

    if a[-1] == b[-1]:
        sub_best, match_string = _lcs(a[:-1], b[:-1], lookup)
        sub_best, match_string = sub_best + 1, match_string + a[-1]

    else:
        l_sub_best, l_match_string = _lcs(a[:-1], b, lookup)
        r_sub_best, r_match_string = _lcs(a, b[:-1], lookup)
        sub_best, match_string = ((l_sub_best, l_match_string)
                                  if l_sub_best >= r_sub_best
                                  else (r_sub_best, r_match_string))
    lookup[(a, b)] = [sub_best, match_string]
    return sub_best, match_string


def lcs_dp(a, b):
    # bottom-up dp approach
    m, n = len(a), len(b)
    matrix = [[0] * (n + 1) for i in range(m + 1)]
    # initialization : m[0][i] = m[i][0] = 0
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if a[r - 1] == b[c - 1]:
                matrix[r][c] = matrix[r - 1][c - 1] + 1

            else:
                matrix[r][c] = max(matrix[r][c - 1], matrix[r - 1][c])
    for i in matrix:
        print i

    return matrix[m][n]


if __name__ == '__main__':
    test_cases = [
        (("", ""), 0),
        (("a", "a"), 1),
        (("bba", "abb"), 2),

    ]
    for test_case, exp in test_cases:
        print lcs_memo(*test_case), exp
        print lcs_dp(*test_case), exp

