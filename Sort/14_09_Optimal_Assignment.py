# optimal task assignment

# sort
# 0 -> n -1
# 1 -> n -2
# etc.


def assignment(arr):
    res = []
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        res.append((arr[left], arr[right]))
        left, right = left + 1, right - 1
    return res

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],

    ]
    for test_case in test_cases:
        print assignment(test_case)