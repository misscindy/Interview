# Sort a k increasing and decreasing array
# [1, 2, 3, 3, 2, 1, 0, 4, 5]


# find all the decreasing intervals and reverse them
# add the result to a list
# merge

def split(arr):
    if len(arr) < 2:
        return sorted(arr)
    lo, high = 0, 1
    sorted_subarray = []
    while high < len(arr):
        while high < len(arr) and arr[high] >= arr[high - 1]:
            high += 1
        sorted_subarray.append(arr[lo: high])

        lo = high
        while high < len(arr) and arr[high] <= arr[high - 1]:
            high += 1
        if lo < high:
            nxt_sub = arr[lo: high]
            nxt_sub.reverse()
            sorted_subarray.append(nxt_sub)
            lo = high
    return sorted_subarray

UP, DOWN = 0, 1


def split_v2(arr):
    start, Dir = 0, UP
    ls_of_ls = []
    for i in range(1, len(arr) + 1):
        if (i == len(arr)
            or (Dir == UP and arr[i - 1] > arr[i])
                or (Dir == DOWN and arr[i - 1] < arr[i])):
            if Dir == UP:
                ls_of_ls.append(arr[start: i])
            else:
                ls_of_ls.append(reverse(arr[start: i]))
            Dir = UP if Dir == DOWN else DOWN
            start = i
    return ls_of_ls


def reverse(arr):
    print arr
    lo, high = 0, len(arr) - 1
    print lo, high
    while lo < high:
        print lo, high
        arr[lo], arr[high] = arr[high], arr[lo]
        lo, high = lo + 1, high - 1
    return arr


if __name__ == '__main__':
    test_cases = [

        ([1, 2, 3, 4, 3, 1, 2, 4]),

    ]
    for test_case in test_cases:
        print split(test_case)
        print split_v2(test_case)



