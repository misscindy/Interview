# implementation of heap
class HeapNodes:
    def __init__(self, data, origin=0):
        self.data = data
        self.origin = origin

    def __repr__(self):
        return "node: %s, origin: %s" % (self.data, self.origin)

    def __cmp__(self, other):
        if self.data > other.data:
            return 1
        elif self.data == other.data:
            return 0
        else:
            return -1


class Heap:
    # Create a heap with ls of nodes or comparables

    def __init__(self, ls=None, is_max=True):
        self.isMax = is_max
        if not ls:
            self.nodes = [None]
            self.size = 0
        else:
            self.size = len(ls)
            ls.insert(0, None)
            self.nodes = ls
            self._build_heap()

    def top(self):
        return self.nodes[1] if not self.is_empty() else None

    def nth(self, k):
        return self.nodes[k]

    def _size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _less(self, left, right):

        return self.nodes[left] < self.nodes[right]

    def _greater(self, left, right):
        return self.nodes[left] > self.nodes[right]

    def compare(self, left, right):
        if self.isMax:
            return self._less(left, right)
        else:
            return self._greater(left, right)

    def sink(self, k):

        while 2 * k <= self.size:
            j = 2 * k
            if j < self.size and self.compare(j, j + 1):
                j += 1
                # pick the greater child if max heap
                # pick the lesser child if min heap
            if not self.compare(k, j):
                break
            # swap
            self.nodes[k], self.nodes[j] = self.nodes[j], self.nodes[k]
            k = j

    def swim(self, k):
        while k > 1 and self.compare(k / 2, k):
            self.nodes[k], self.nodes[k / 2] = self.nodes[k / 2], self.nodes[k]
            k /= 2

    def insert(self, x):
        self.size += 1
        self.nodes.append(x)
        self.swim(self.size)

    def pop_top(self):
        # delete min or max
        if self.size < 1:
            return
        self.nodes[1], self.nodes[self.size] = self.nodes[self.size], self.nodes[1]
        self.size -= 1
        self.sink(1)
        return self.nodes.pop()

    def _build_heap(self):
        for i in xrange(self.size / 2, 0, -1):
            self.sink(i)

    def __repr__(self):
        return "%s" % self.nodes


if __name__ == '__main__':

    # min_heap = Heap([1, 2, 4, 3, 8], False)
    # print min_heap
    # max_heap = Heap([1, 2, 4, 10])
    # print max_heap
    heap_nodes = [(1, 1), (2, 2), (3, 3), (8, 8)]
    heap_nodes_input = []
    for (a, b) in heap_nodes:
        a_node = HeapNodes(a, b)
        heap_nodes_input.append(a_node)

    # max_heap2 = Heap(heap_nodes_input)
    # print max_heap2
    print "==========Node ==========="
    print heap_nodes_input
    print "==========Node ==========="
    min_heap2 = Heap(heap_nodes_input, False)
    print min_heap2
    print min_heap2.pop_top()
    print min_heap2

    c = Heap(is_max=False)
    c.insert(3)
    c.insert(4)
    c.insert(1)
    c.insert(2)
    print c




