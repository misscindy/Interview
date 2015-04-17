class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        codes = {i for i in range(1, 27)}
        if not s or s[0] not in codes:
            return 0
        s = "0" + s
        prev, current, nxt = 1, 1, 0
        print s
        for i in range(1, len(s)):
            if s[i] in codes:
                nxt = prev + current if s[i-1:i+1] in codes else current
            else:
                if s[i-1:i+1] in codes:
                    nxt = prev
                else:
                    return 0
            prev, current = current, nxt

        return current





a = Solution()
print a.numDecodings("1")