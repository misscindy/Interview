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


def add_interval(intervals, new_i):
    new_start, new_end = new_i.start, new_i.end
    runner = 0
    while runner < len(intervals) and intervals[runner].end < new_start:
        runner += 1
    start = runner
    while runner < len(intervals) and intervals[runner].start <= new_end:
        new_start = min(intervals[runner].start, new_start)
        new_end = max(intervals[runner].end, new_end)
        runner += 1
    print start, runner
    intervals[start: runner] = [Interval(new_start, new_end)]

    return intervals



if __name__ == "__main__":
    test_cases = [
        # ([Interval(0, 3), Interval(0, 3), Interval(0, 3)], 3),
        # ([Interval(0, 1), Interval(2, 3), Interval(4, 5)], Interval(1, 2)),
        # ([Interval(0, 0), Interval(2, 3), Interval(4, 5)], Interval(1, 1)),
        # ([Interval(0, 0)], Interval(1, 1)),
        # ([Interval(0, 0)], Interval(1, 2)),
        ([Interval(2, 4)], Interval(0, 1)),


    ]
    for test_case, exp in test_cases:
        print add_interval(test_case, exp)

