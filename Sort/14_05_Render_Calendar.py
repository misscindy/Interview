# render calender
# given a set of events with (start, end) time interval
# return the maximum # of events happening concurrently


class Interval(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __cmp__(self, other):
        if self.start > other.start:
            return 1
        elif self.start < other.start:
            return -1
        else:
            return 0

    def __repr__(self):
        return "start: %i  ends: %i"%(self.start, self.end)


def max_overlap(intervals):
    # O(n^2)
    # check end pts 
    if len(intervals) < 2:
        return len(intervals)
    max_count = 0
    for ndx, cur_i in enumerate(intervals):
        cur_start, cur_end = cur_i.start, cur_i.end
        count, count2 = 0, 0
        for other_i in intervals:
            if other_i.start <= cur_start <= other_i.end:
                count += 1
            if other_i.start <= cur_end <= other_i.end:
                count2 += 1
        max_count = max(max_count, count2, count)

    return max_count


def max_overlap_2(intervals):
    def comparator(x, y):
        if x[0] > y[0]:
            return 1
        elif x[0] < y[0]:
            return -1
        else:
            if x[1] > y[1]:
                return 1
            elif x[1] < y[1]:
                return -1
            else:
                return 0
    # O(n)
    timeline = []
    for i in intervals:
        timeline.append((i.start, 0))
        timeline.append((i.end, 1))
    timeline.sort(cmp=comparator)
    count, max_count = 0, 0
    for v, type in timeline:
        if type == 0:
            count += 1
        else:
            count -= 1
        max_count = max(count, max_count)
    print timeline
    return max_count

if __name__ == "__main__":
    test_cases = [
        # ([Interval(0, 3), Interval(0, 3), Interval(0, 3)], 3),
        ([Interval(0, 1), Interval(2, 3), Interval(0, 3)], 2),
        # ([Interval(0, 1), Interval(1, 2), Interval(3, 3)], 2),

    ]
    for test_case, exp in test_cases:
        print max_overlap(test_case), exp
        print max_overlap_2(test_case), exp

