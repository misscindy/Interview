class Solution:

# @param s, a string
# @return a list of strings
    def findRepeatedDnaSequences(self, s):
        repeatSeq = set()
        addedSeq = set()
        result = []
        answer = []
        charToBin = {'A' : 0b00, 'T' : 0b01, 'G' : 0b10, 'C' : 0b11}
        mask = 0xfffff
        current = 0
        for i in range(len(s)):
        #create bit
            x = charToBin[s[i]]
            current |= x
            if i >= 9:
                print bin(current)
                if current in repeatSeq:
                    if current not in addedSeq:
                        addedSeq.add(current)
                        result.append(i - 9)
                else:
                    repeatSeq.add(current)
        #shift
            current <<= 2
        #mask
            current &= mask
        for i in result:
            answer.append(s[i : i + 10])
        return answer


if __name__ == '__main__':
    a = Solution()

    print a.findRepeatedDnaSequences("AAAAAGGGGGAAAAAGGGGG")