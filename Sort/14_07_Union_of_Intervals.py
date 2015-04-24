# merge intervals
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
            if self.end > other.end:
                return 1
            elif self.end < other.end:
                return -1
            else:
                return 0

    def __repr__(self):
        return "start: %i  ends: %i" % (self.start, self.end)


def merge(intervals):
    intervals.sort()



