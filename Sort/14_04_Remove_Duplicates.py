
# def unique(arr):
#     if len(arr) < 2:
#         return arr
#     head, i, j = 0, 0, 0
#     while j < len(arr):
#         # print head, i, j
#         if arr[j] == arr[i]:
#             j += 1
#         else:
#
#             # found some dup
#             print head, i, j, j - i
#             if j - i > 1:
#                 i = j
#             else:
#                 arr[head] = arr[i]
#                 i = j
#                 head += 1
#     return head - 1


def unique(arr):
    if len(arr) < 2:
        return
    head = 0
    for ndx, element in enumerate(arr):
        if ((ndx == 0 and element != arr[1])
            or (ndx == len(arr) - 1 and element != arr[len(arr) - 2])
                or (element not in (arr[ndx - 1], arr[ndx + 1]))):
            arr[head] = element
            head += 1
    return head - 1




if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 3], sorted([1, 2, 1, 3, 3, 3])),
        ([3, 2, 5, 4, 3, -2, 1], sorted([2, 2, 3, -2, 1])),

        # ([1, -2, -5], sorted([1, -2, -5])),
        # ([], sorted([])),

        # ([1], sorted([1])),
        ]
    for test_case, exp in test_cases:
        print exp
        print unique(exp)
        print exp







