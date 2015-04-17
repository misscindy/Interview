class Solution:
    # @param s1, a string
    # @param s2, a string
    # @param s3, a string
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1) + 1, len(s2) +  1
        if (m + n - 2) != len(s3) :
            return False
        # (0, 0, True) (0, 1, ....)
        # (1, 0, ....)
          #s1 s2
        matrix = [[False] * n for i in range(m)]
        matrix[0][0] = True
        for ndx in range(1, m):
            if s3[ndx - 1] == s1[ndx - 1] and matrix[ndx - 1][0]:
                matrix[ndx][0] = True

        for ndx in range(1, n):
            if s3[ndx - 1] == s2[ndx - 1] and matrix[0][ndx - 1]:
                matrix[0][ndx] = True

        for r in range(1, m):
            for c in range(1, n):
                print r, c
                if (s3[r + c - 1] == s1[r - 1] and matrix[r - 1][c]) or (s3[r + c - 1] == s2[c - 1] and matrix[r][c - 1]):
                    matrix[r][c] = True
        print matrix
        return matrix[m - 1][n - 1]
a = Solution()

a.isInterleave("a", "b", "ab")