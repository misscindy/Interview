from heapq import *


def median():
    max_heap, min_heap = [], []
    nxt_val = raw_input("nxt > ")
    while nxt_val != "":
        heappush(min_heap, float(nxt_val))
        if len(min_heap) > len(max_heap) + 1:
            heappush(max_heap, -heappop(min_heap))
            print max_heap, min_heap
        print min_heap[0] if len(min_heap) > len(max_heap) else (min_heap[0] - max_heap[0]) / float(2)
        nxt_val = raw_input("nxt > ")


median()