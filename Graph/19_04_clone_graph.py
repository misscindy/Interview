import collections
# clone graph


class Vertex(object):

    def __init__(self, v):
        self.v = v
        self.neighbors = set()

    def add_neighbor(self, v):
        self.neighbors.add(v)


def clone(v):
    built = dict()

    def _clone(v, built):
        if not v:
            return None
        if v in built:
            return built[v]
        clone_node = Vertex(v)
        built[v] = clone_node
        for n in v.neighbors:
            clone.node.neighbor.add(_clone(n, built))
        return clone_node

    return _clone(v, built)




