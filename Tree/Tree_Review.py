# Regular Tree
# Traversal


from util import *

# 10_02 k-balanced


def is_k_balanced(node, k):
    if not node:
        return [None, 0]

    left_res, node_num = is_k_balanced(node.left, k)
    if left_res:
        return [left_res, 0]

    right_res, r_node_num = is_k_balanced(node.right, k)
    if right_res:
        return [right_res, 0]

    # not found yet

    if abs(node_num - r_node_num) <= k:
        return [None, node_num + r_node_num + 1]

    else:
        return [node, 0]


# 10_03 symmetric
# todo Iterative?


def is_symmetric(node):
    return not node or is_sym(node.left, node.right)


def is_sym(left, right):
    if (not left) and (not right):
        return True

    elif left and right:
        return left.val == right.val and is_sym(left.left, right.right) and (is_sym(left.right), right.left)
    return False


# 10_04 LCA

def lca(root, node1, node2):
    if not root:
        return [None, 0]

    left_res, found = lca(root.left, node1, node2)
    if found > 1:
        return left_res, found
    right_res, r_found = lca(root.right, node1, node2)
    if r_found > 1:
        return lca(right_res, r_found)

    root_count = (1 if root in (node1, node2) else 0) + found + r_found
    return [root, root_count] if root_count > 1 else [None, root_count]


# 10_06_BinaryPath_sum


def path_sum(root):
    return _sum(root, 0)


def _sum(root, cur_sum):
    if not root:
        return 0

    if not root.left and not root.right:
        return cur_sum * 2 + root.val

    return _sum(root.left, cur_sum*2 + root.val) + _sum(root.right, cur_sum * 2 + root.val)

# 10_07_BinaryPath_sum
# Iterative & All Path


def exist_path_sum(root, target):
    return _exist_path_sum(root, 0, target)


def _exist_path_sum(root, cur_sum, target):
    if not root:
        return False

    if not root.left and not root.right:
        return target == cur_sum + root.val
    else:
        return (_exist_path_sum(root.left, cur_sum + root.val, target)
                or _exist_path_sum(root.right, cur_sum + root.val, target))


# 10_08_kth_node
def _find_kth(tree, k):

    cur_node = tree
    while tree:
        l_size = 0 if not cur_node.left else cur_node.left.size
        if l_size == k - 1:
            return cur_node
        elif l_size < k - 1:
            cur_node = cur_node.right
            k -= (l_size + 1)
        else:
            cur_node = cur_node.left

    return None


# 10_09_in_order_traversal


def in_order_r(node):
    if not node:
        return
    else:
        in_order_r(node.left)
        print node.val,
        in_order_r(node.right)


def in_order_s(node):
    stack, runner = [], node
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print node.val,
            node = node.right


def in_order_p(node):
    prev, runner = None, node
    while runner:
        # nxt = None
        if not prev or prev.left == runner or prev.right == runner:
            # came down from root to current
            if runner.left:
                nxt = runner.left
            else:
                print runner.val
                nxt = runner.right if runner.right else runner.parent
        elif runner.left == prev:
            nxt = runner.right if runner.right else runner.parent

        else:
            nxt = runner.parent
        prev = runner
        runner = nxt


# iterative pre order

def pre_order_i(node):
    runner, stack = node, []
    while runner or stack:
        if runner:
            print runner.val,
            stack.append(runner)
            runner = runner.left
        else:
            runner = stack.pop().right

# 10.10 iterative post order


def pre_order_i_2(node):
    if not node:
        return
    stack = [node]
    while stack:
        nxt = stack.pop()
        print nxt.val,
        if nxt.right:
            stack.append(nxt.right)
        if nxt.left:
            stack.append(nxt.left)


def post_order(node):
    stack, prev = [node], None
    while stack:
        curr = stack[-1]
        if not prev or prev.left == curr or prev.right == curr:
            # came down from prev
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
            else:
                print curr.val,
                stack.pop()
        elif curr.left == prev:
            if curr.right:
                stack.append(curr.right)
            else:
                print curr.val,
                stack.pop()
        else:
            print curr.val,
            stack.pop()
        prev = curr


def post_order_r(node):
    if not node:
        return
    post_order_r(node.left)
    post_order_r(node.right)
    print node.val,


# 10.11 compute successor

def nxt(node):
    # node has parent
    # case has a right child
    if node.right:
        runner = node.right
        while runner.left:
            runner = runner.left
        return runner

    # case does not have a right child
    runner = node
    while runner.parent and runner.parent.right == runner:
        runner = runner.parent
    return runner.parent


# todo reconstructs 10.12, 10.13


# Compute linked list from leaves

def conn_leaves_w(root):
    dummy_head = ListNode(-1)
    tail = [dummy_head]
    conn_leaves(root, tail)
    printLinkedList(dummy_head)


def conn_leaves(root, tail):
    if not root:
        return

    if not root.left and not root.right:
        tail[0].next = ListNode(root)
        tail[0] = tail[0].next
    else:
        conn_leaves(root.left, tail)
        conn_leaves(root.right, tail)


# Implement Locking


class BinaryTreeNode(object):

    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False
        self.num_of_locked_child = 0

    def _is_lock(self):
        return self.locked

    def lock(self):
        if self.locked or self.num_of_locked_child > 0:
            return False

        # check ancestors
        runner = self.parent
        while runner:
            if runner.locked:
                return False
            runner = runner.parent

        # lock
        self.locked = True
        runner = self.parent
        while runner:
            runner.num_of_locked_child += 1
            runner = runner.parent
        return True

    def unlock(self):
        self.locked = False
        runner = self.parent
        while runner:
            runner.num_of_locked_child -= 1
            runner = runner.parent


def right_side(root, res):
    if not root:
        return
    res.append(root.val)
    if root.right:
        right_side(root.right, res)
    else:
        right_side(root.left, res)




if __name__ == "__main__":
    tree = createBinarySearchTreeNotBalanced([1, 2, 3, 4,5, 4, 4, 1, 2])
    # printBinarySearchTree(tree)
    # print is_k_balanced(tree, 2)
    values = [4, 5, 5, 7, 2, 1, 3]
    bst = createBinarySearchTree(values)
    # print bst.left.left.val, bst.left.right.val
    # print "LCA: ", lca(bst, bst.left.left, bst.left.right)[0].val
    # print bst.left.val, bst.right.val
    # print "LCA: ", lca(bst, bst.right, bst.left)[0].val
    # print '=== Binary Tree ==='
    # values = [0, 1, 0, 0, 1, 1, 0, 1]
    # bt = createBinaryTree(values)
    # print path_sum(bt)
    # printBinarySearchTree(bt)
    # print exist_path_sum(bt, 3)
    # print exist_path_sum(bt, 2)
    # print exist_path_sum(bt, 4)
    # print exist_path_sum(bt, 0)
    # printBinarySearchTree(bst)
    # print exist_path_sum(bst, 4)
    # print exist_path_sum(bst, 7)
    # print exist_path_sum(bst, 6)
    # tree = createBinarySearchTree([1, 2, 3, 4])
    # printBinarySearchTree(tree)
    # tree.left.size = 1
    # tree.right.right.size = 1
    # tree.right.size = 2
    # tree.size = 1 + tree.left.size + tree.right.size
    # print _find_kth(tree, 4)
    # printBinarySearchTree(bst)
    # in_order_s(bst)
    # print
    # pre_order_i(bst)
    # print
    # pre_order_i_2(bst)
    # print "post"
    # post_order_r(bst)
    # print
    # post_order(bst)
    # print "Compute Successor"
    # printBinarySearchTree(bst)
    # print nxt(bst)
    # print nxt(bst.left)
    # print nxt(bst.left.left)
    # print nxt(bst.left.right)
    # print "Connect Leaves"
    # conn_leaves_w(bst)
    result = []
    printBinarySearchTree(tree)
    right_side(tree, result)
    print result
