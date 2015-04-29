# Stack & Queue Review


# 9.3 valid paren


# 9.4 Longest Valid Paren
# "(()))(()())"
def longest_valid(s):
    left_p, max_len, end = [], 0, -1

    for ndx, p in enumerate(s):
        if p == "(":
            left_p.append(ndx)
        # see a ")"
        else:
            if not left_p:
                end = ndx
            else:
                left_p.pop()
                start = end if not left_p else left_p[-1]
                max_len = max(max_len, ndx - start)
    return max_len




# 9.5 simplify path


# 9.6 print bst
def load_src(name, fpath):
    import os, imp
    p = fpath if os.path.isabs(fpath) \
        else os.path.join(os.path.dirname(__file__), fpath)
    return imp.load_source(name, p)

util = load_src("util", "../Tree/util.py")


def print_bst(node):
    tn = util.TreeNode()




# 9.7 search posting list


class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None
        self.order = -1

    def __repr__(self):
        rand = self.random.val
        return "Node(%i): %i " % (rand, self.val)


def jump_first(head):
    _visit(head, [0])


def _visit(node, cur_order):
    if node and node.order == -1:
        node.order = cur_order[0]
        cur_order[0] += 1
        _visit(node.random, cur_order)
        _visit(node.next, cur_order)


def jump_first_i(head):
    order, stack = 0, [head]
    while stack:
        nxt = stack.pop()
        if nxt.order == -1:
            nxt.order = order + 1
            order += 1
            if nxt.next:
                stack.append(nxt.next)
            if nxt.random:
                stack.append(nxt.random)







# 9.8 sunset view stream

def out_put_sunsets():
    bldgs = []
    nxt = raw_input("nxt building height > ")
    while nxt != "":
        newbie = int(nxt)
        while bldgs and newbie >= bldgs[-1]:
            bldgs.pop()
        bldgs.append(newbie)
        nxt = raw_input("nxt building height > ")
    for i in bldgs:
        print i,
    print



# 9.9
# sort a stack


def sort(stack):

    if not stack:
        return
    top = stack.pop()
    sort(stack)
    insert(top, stack)


def insert(val, stack):
    if not stack or stack[-1] >= val:
        stack.append(val)

    else:
        top = stack.pop()
        insert(val, stack)
        stack.append(top)


if __name__ == '__main__':
    a = [1, 2, 3, 2, 5, 2]
    sort(a)
    print a
    print "9.8"
    out_put_sunsets()
    print "9.7"
    head = RandomListNode(0)
    first = RandomListNode(1)
    sec = RandomListNode(2)
    third = RandomListNode(3)
    head.next, head.random = first, sec
    first.next, first.random = sec, head
    sec.next, sec.random = third, third
    third.next, third.random = None, sec
    # runner = head
    # while runner:
    # print runner,
    # 	runner = runner.next

    # print
    jump_first_i(head)
    #jump_first(head, 0)
    runner = head
    while runner:
        print runner, "order : ", runner.order
        runner = runner.next
    print "Longest valid paren"
    test_cases = ["(())", "()(", ")))()"]
    for i in test_cases:
        print longest_valid(i)

