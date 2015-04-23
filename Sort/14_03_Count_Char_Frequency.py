import collections
# M1: sort and count
# M2: Store in char array or dictionary


def count_chr(s):
    counts = collections.defaultdict(int)
    for c in s:
        counts[c] += 1
    return sorted(counts.items(), key=lambda x: x[0])


def count_chr2(s):
    s = sorted(s)
    res = []
    count = 0
    for i, char in enumerate(s):
        if i == 0 or char == s[i - 1]:
            count += 1
        else:
            res.append((s[i - 1], count))
            count = 1
    if count:
        res.append((s[-1], count))
    return res


if __name__ == "__main__":
    test_cases = [
        ("acckkkaaacsdfas", sorted("acckkkaaacsdfas")),
        ("aaa", sorted("aaa")),
        ("", sorted("")),


    ]
    for s, exp in test_cases:
        print count_chr2(s), exp