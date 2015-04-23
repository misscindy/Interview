"""
Description:
    @ Mock
    @ param int [] -> [1, 5, 0, 6]
    @ param int -> 21
    @ return int [[15, 06]]

"""


def match1(digits, target):

    def _match(digits, target, cur_ndx, cur_sum, partial, result):
        if cur_ndx == len(digits):
            if cur_sum == target:
                result.append(partial[:])
            return
        if cur_sum > target:
            return

        for i in range(cur_ndx, len(digits)):
            # create the nxt int
            nxt = 0
            for j in range(cur_ndx, i + 1):
                nxt = nxt * 10 + digits[j]
            if nxt:
                _match(digits, target, i + 1, nxt + cur_sum, partial + [nxt], result)
    result = []
    _match(digits, target, 0, 0, [], result)
    return result

if __name__ == "__main__":

    test_cases = [
        (([1, 5, 0, 6], 21), [[15, 6]]),
        (([1, 0, 6], 1), []),
        (([0, 0, 1], 1), [[1]]),
        (([1, 1], 11), [11]),

    ]
    for test_case, exp in test_cases:
        print match1(*test_case), exp





