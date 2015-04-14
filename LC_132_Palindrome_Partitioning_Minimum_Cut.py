# Palindrome Partitioning
# Minimum Cut


def min_cut(s):
    dp_table = [-1, 0]
    # print "hello"
    # print len(s)
    for length in range(2, len(s) + 1):

        entry = 1 + dp_table[length - 1]
        # fill out dp_table[length]
        for left in range(length):
            if isP(s[left: length]):
                entry = min(entry, dp_table[left] + 1)
        dp_table.append(entry)
    return dp_table




def isP(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i + 1, j - 1
    return True

if __name__ == '__main__':
    test_cases = [
        # ([""], 0),
        # (["a"], 0),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 0),


    ]
    for test, exp in test_cases:
        print min_cut(test)[len(test)] == exp
        print min_cut(test)


    isp_table = [[None]]


