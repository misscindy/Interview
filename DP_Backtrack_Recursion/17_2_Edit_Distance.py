'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''


def edit_dst(a, b):
    return _edit_dst(a, b, dict())


def _edit_dst(a, b, lookup):
    if (a, b) in lookup:
        return lookup[(a, b)]

    if len(a) == 0 or len(b) == 0:
        return max(len(a), len(b))

    if a[-1] == b[-1]:
        min_edit = _edit_dst(a[:-1], b[:-1], lookup)

    else:
        min_edit = min(_edit_dst(a[:-1], b, lookup), _edit_dst(a, b[:-1], lookup), _edit_dst(a[:-1], b[:-1], lookup)) + 1
    lookup[(a, b)] = min_edit
    return min_edit


def edit_dst_dp(a, b):
    m, n = len(a), len(b)
    # convert b to a
    matrix = [[0] * (n + 1) for i in range(m + 1)]
    for r in range(m + 1):
        for c in range(n + 1):
            # base cases
            if r == 0:
                matrix[r][c] = c
                continue
            if c == 0:
                matrix[r][c] = r
                continue
            # other cases
            if a[r - 1] == b[c - 1]:
                matrix[r][c] = matrix[r - 1][c - 1]
            else:
                matrix[r][c] = min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]) + 1
    for i in matrix:
        print(i)
    return matrix[m][n]


def edit_save_space(a, b):
    if len(a) < len(b):
        return edit_save_space(b, a)
    m, n = len(a), len(b)
    prev_row = [0] * (n + 1)
    # prev_row = [i for i in range(n + 1)]
    print prev_row
    for i in range(1, m + 1):
        i_1_j_1 = prev_row[0]
        prev_row[0] = i
        for j in range(1, len(prev_row)):
            i_1_j = prev_row[j]
            prev_row[j] = i_1_j_1 if a[i - 1] == b[j - 1] else 1 + min(i_1_j_1, i_1_j, prev_row[j - 1])
            i_1_j_1 = i_1_j
        print prev_row
    return prev_row[-1]









if __name__ == '__main__':
    test_cases = [
        # (("", ""), 0),
        # (("a", "a"), 0),
        # (("bba", "abb"), 2),
        # (("abba", "abb"), 1),
        # (("abbaccc", "abbcccabbaccc"), 6),
        (("acxxxc", "bbcccabbc"), 7),
        (("a", "b"), 1),
        (("bc", "abc"), 2),

    ]
    for test_case, exp in test_cases:
        print edit_dst(*test_case), exp
        print edit_save_space(*test_case), exp

