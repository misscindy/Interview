

def largest(height):
    stack, max_area = [], 0
    for i in range(len(height) + 1):
        while stack and (i == len(height) or height[stack[-1]] > height[i]):
            last_h = height[stack.pop()]
            max_area = max(max_area, last_h * (i if not stack else i - stack[-1] - 1))
        stack.append(i)
    return max_area


def largest_n_2(height):
    max_area = 0

    for start in range(len(height)):
        running_min = height[start]
        for j in range(start, len(height)):
            running_min = min(height[j], running_min)
            max_area = max(max_area, running_min * (j - start + 1))
    return max_area



if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 4),
        ([2, 4], 4),
        ([4, 4], 8),
        ([1, 2, 3, 4, 5, 6], 12),

    ]
    for test_case, exp in test_cases:
        print "largest: ", largest(test_case), exp
        print "largest_n_2: ", largest_n_2(test_case), exp