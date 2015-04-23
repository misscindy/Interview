
def is_match(string, s_start, pattern, p_start):

    if s_start == len(string) and p_start == len(pattern):
        return True
    if p_start >= len(pattern):
        return False

    if pattern[p_start] == "?":
        return is_match(string, s_start + 1, pattern, p_start + 1) or is_match(string, s_start, pattern, p_start + 1)

    elif pattern[p_start] == "*":
        if s_start >= len(string):
            return is_match(string, s_start, pattern, p_start + 1)
        else:
            if is_match(string, s_start, pattern, p_start + 1):
                return True
            wild_char = string[s_start]
            offset = 0
            while s_start + offset < len(string) and string[s_start + offset] == wild_char:
                if is_match(string, s_start + offset + 1, pattern, p_start + 1):
                    return True
                offset += 1
            return False
    elif s_start < len(string) and pattern[p_start] == string[s_start]:
        return is_match(string, s_start + 1, pattern, p_start + 1)
    else:
        return False


class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        # dp
        m, n = len(p) + 1, len(s) + 1
        matrix = [[False] * n for i in range(m)]
        matrix[0][0] = True
        # p_len == 0,  [True, False, False, False]
        i = 0

        while i < len(p) and p[i] in ["?", "*"]:
            matrix[i+1][0] = True
            i += 1
        print matrix
        for p_len, row in enumerate(matrix):
            if p_len == 0:
                continue

            for s_len, col in enumerate(row):
                if s_len == 0:
                    continue
                pattern_char = p[p_len - 1]
                if pattern_char == "?":
                    entry = (matrix[p_len - 1][s_len]
                                        or matrix[p_len - 1][s_len - 1])
                elif pattern_char == "*":
                    entry = matrix[p_len - 1][s_len - 1]
                    wild_char = s[s_len - 1]
                    start = s_len
                    while start < len(s) + 1 and s[start - 1] == wild_char:
                        entry = (entry or matrix[p_len - 1][start])
                        start += 1
                elif pattern_char == s[s_len - 1] and matrix[p_len - 1][s_len - 1]:
                    entry = True
                else:
                    entry = False
                matrix[p_len][s_len] = entry
        print matrix
        return matrix[m-1][n-1]

def isMatch_rolling(s, p):
        l = len(s)
        if len(p) - p.count('*') > l:
            return False
        dp = [True] + [False] * l
        for letter in p:
            new_dp = [dp[0] and letter == '*']
            print new_dp
            if letter == '*':
                for j in range(l):
                    new_dp.append(new_dp[-1] or dp[j + 1])
            elif letter == '?':
                new_dp += dp[:l]
            else:
                new_dp += [dp[j] and s[j] == letter for j in range(l)]
            dp = new_dp
        return dp[-1]


if __name__ == "__main__":
    test_cases = [
        # (("aa", "aa"), True),
        # (("aaa", "aa"), False),
        # (("aab", "c*a*b"), False),
        # (("aa", "a?"), True),
        # (("abba", "a*ba"), True),
        # (("aa", "a*ba"), False),
        # (("aa", "*?"), True),
        # (("ab", "a*b"), True),
        # (("", "*b"), False),
        # (("", "*"), True),
        # # (("aaa", ""), False),
        # (("aabb", "*?aa*"), False),
        (("abaa", "a*"), False),

    ]
    a = Solution()

    for (s, p), exp in test_cases:
        print a.isMatch(s,p)
              # == exp

