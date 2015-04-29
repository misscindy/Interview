# almost sorted array
from heapq import *


def sort(k):
    # push the first k on to heap
    nxt = input("Nxt >: ")
    i = 0
    min_heap = []
    while nxt is not None and i < k:
        heappush(min_heap, nxt)
        i += 1
        nxt = input("Nxt >: ")
    while nxt is not None:
        heappush(min_heap, nxt)
        print(heappop(min_heap))
        nxt = input("Nxt >: ")
    while min_heap:
        print heappop(min_heap)


def sort_2(k):
    nxt = raw_input("Nxt > ")

    min_heap = []
    while nxt != "":
        heappush(min_heap, int(nxt))
        if len(min_heap) > k:
            print heappop(min_heap)
        nxt = raw_input("Nxt > ")
    while min_heap:
        print heappop(min_heap)

sort_2(2)



