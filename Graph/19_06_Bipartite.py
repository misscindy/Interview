import collections


class Vertex(object):

    def __init__(self, v):
        self.v = v
        self.d = -1
        self.neighbors = set()

    def add_neighbor(self, v):
        self.neighbors.add(v)

    def __repr__(self):
        return str(self.v) + " " + str(self.d) + " "


def is_bipartite(vertex):
    if not vertex:
        return False
    vertex.d = 0
    q = collections.deque()
    q.append(vertex)

    while q:
        cur_node = q.popleft()
        print cur_node
        for n in cur_node.neighbors:
            if n.d == -1:
                n.d = cur_node.d + 1
                q.append(n)
            elif n.d == cur_node.d:
                return False
    print vertex.neighbors
    return True

if __name__ == "__main__":
    #
    graph = Vertex(0)
    for i in range(1, 4):
        graph.add_neighbor(Vertex(i))
    a = graph.neighbors.pop()
    graph.add_neighbor(a)
    a.add_neighbor(graph)

    print is_bipartite(graph)
    print graph.neighbors
    for i in graph.neighbors:
        print i.neighbors