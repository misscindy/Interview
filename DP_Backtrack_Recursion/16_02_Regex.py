
# todo dp solution, memo

def regex(s, pattern):
    pass


def _regex(s, pattern):
    # print s, pattern
    if not pattern:
        return not s

    if len(pattern) > 1 and pattern[1] == "*":

        return (_regex(s, pattern[2:])
                or ((s != "" and (s[0] == pattern[0] or pattern[0] == ".")) and _regex(s[1:], pattern))
                )
    else:
        return (s != "" and (s[0] == pattern[0] or pattern[0] == '.')) and _regex(s[1:], pattern[1:])


if __name__ == "__main__":
    test_cases = [
        (("aa", "aa"), True),
        (("aaa", "aa"), False),
        (("aab", "c*a*b"), True),
        (("aa", "a."), True),
        (("abba", "a*ba"), False),
        (("aa", "a*ba"), False),
        (("ab", ".*"), True),
        (("ab", "a*b"), True),
        (("", "*b"), False),
        (("", "*"), False),
        (("aaa", ""), False),
        (("aabb", "*?aa*"), False),
        (("abaa", "a*"), False),

    ]


    for (s, p), exp in test_cases:
        print _regex(s,p), exp

              # == exp



