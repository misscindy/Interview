import random
import math


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return "Node: %i" % self.val

    def __repr__(self):
        return "Node(%i)" % self.val


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1

    def __repr__(self):
        return "Node: %i " % self.val


def createLinkedList(vs, rand=False, uni=False, size=10):
    """
        Create a LinkedList.
        Argus:
            vs - a list of values.
            random - whether or not to generate a LinkedList with random values.
            unique - a random generated LinkedList with unique values.
            size - default size of a random LinkedList is 15.
    """
    dummy = ListNode(-1)
    runner = dummy
    if rand:
        random_range = size * 2
        if uni:
            vs_set = set()
            while size > 0:
                num = int(random_range * random.random())
                if num not in vs_set:
                    runner.next = ListNode(num)
                    runner = runner.next
                    size -= 1
                    vs_set.add(num)
            return dummy.next
        else:
            vs = [int(random_range * random.random()) for i in xrange(random_range)]
    for v in vs:
        runner.next = ListNode(v)
        runner = runner.next
    return dummy.next


def printLinkedList(linked_list):
    """
        Print a LinkedList
        Args:
            linked_list - the LinkedList to print out
    """
    vs = []
    while linked_list:
        vs.append(str(linked_list.val))
        linked_list = linked_list.next
    print ' -> '.join(vs)


def isSameLinkedList(linked_list1, linked_list2):
    """
        Check whether two linked lists are the same.
        Args:
            linked_list1: -
            linked_list2: -
    """
    while linked_list1:
        if linked_list1.val != linked_list2.val:
            return False
        linked_list1, linked_list2 = linked_list1.next, linked_list2.next
    return True


def createBinaryTree(vs):
    """
        Generate a binary tree based on the given array.
        (!important: using '-1' to indicate null node)

        Args:
            vs - an integer array

        {0, 1, 2, 3, -1, 4, -1}

                0
               /  \
              1    2
             / \  / \
            3  # 4   #
    """

    def _helper(node, vs, index):
        left = index * 2 + 1
        right = left + 1
        if left >= len(vs):
            return None
        if vs[left] == -1:
            node.left = None
        else:
            node.left = TreeNode(vs[left])
            node.left.parent = node

        if right >= len(vs):
            return None
        if vs[right] == -1:
            node.right = None
        else:
            node.right = TreeNode(vs[right])
            node.right.parent = node

        if node.left:
            _helper(node.left, vs, left)
        if node.right:
            _helper(node.right, vs, right)

    if not vs:
        return None
    root = TreeNode(vs[0])
    _helper(root, vs, 0)
    return root


def createBinarySearchTree(vs):
    """
        Generate a balanced binary search tree based on the given array.

        Args:
            vs - an integer array

        {4, 5, 5, 7, 2, 1, 3}

                4
               /  \
              2    5
             / \  / \
            1  3 5   7
    """

    def _helper(vs, left, right):
        if left > right:
            return None
        mid = (left + right) >> 1
        node = TreeNode(vs[mid])
        node.left = _helper(vs, left, mid - 1)
        if node.left:
            node.left.parent = node
        node.right = _helper(vs, mid + 1, right)
        if node.right:
            node.right.parent = node
        return node

    vs = sorted(vs)
    root = _helper(vs, 0, len(vs) - 1)
    return root


def createBinarySearchTreeNotBalanced(vs):
    """
        Generate a not balanced binary search tree based on the given array.

        Args:
            vs - an integer array

        {3, 5, 5, 7, 4, 1, 2}

                 3
               /   \
              1     5
               \   / \
                2 5   7
                 /
                4
    """
    if not vs:
        return None
    root = TreeNode(vs[0])
    for v in vs[1:]:
        runner = root
        while True:
            if v <= runner.val:
                if not runner.left:
                    runner.left = TreeNode(v)
                    runner.left.parent = runner
                    break
                else:
                    runner = runner.left
            else:
                if not runner.right:
                    runner.right = TreeNode(v)
                    runner.right.parent = runner
                    break
                else:
                    runner = runner.right
    return root


def createCompleteBinarySearchTree(vs):
    """
        Generate a complete binary search tree based on the given array. Array is already sorted.

        Args:
            vs - an integer array

        {1, 2, 3, 4, 5}

                 4
               /   \
              2     5
             / \
            1   3
    """

    def _getRootIndex(left, right):
        left, right = left + 1, right + 1
        n = right - left + 1
        h_left = math.floor(math.log(n, 2))
        h_right = 1 if h_left - 1 else h_left - 1
        # case 1 - right last level empty
        if n <= 1 + math.pow(2, h_left) - 1 + math.pow(2, h_right) - 1:
            return (right - 1) - (math.pow(2, h_right) - 1)
        else:
            return (left - 1) + (math.pow(2, h_left) - 1)

    def _helper(vs, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(vs[left])
        if left + 1 == right:
            node = TreeNode(vs[right])
            node.left = TreeNode(vs[left])
            return node
        i = int(_getRootIndex(left, right))
        node = TreeNode(vs[i])
        if left < right:
            node.left = _helper(vs, left, i - 1)
            node.right = _helper(vs, i + 1, right)
        return node

    if not vs:
        return None
    return _helper(vs, 0, len(vs) - 1)


def printBinarySearchTree(root):
    def _print(root, level):
        if not root:
            return
        _print(root.right, level + 1);
        if level:
            for i in xrange(level - 1):
                print '|\t',
            print '|-------', root.val
        else:
            print root.val
        _print(root.left, level + 1)

    _print(root, 0)


if __name__ == '__main__':
    values = [1, 3, 5, 7, 9]
    ll = createLinkedList(values)
    ll = createLinkedList(values, rand=True, uni=True, size=5)
    printLinkedList(ll)

    print '\n'
    print '=== Binary Tree ==='
    values = [0, 1, 2, 3, -1, 4, -1]
    bt = createBinaryTree(values)
    printBinarySearchTree(bt)

    print '\n'
    print '=== Binary Search Tree ==='

    values = [4, 5, 5, 7, 2, 1, 3]
    bst = createBinarySearchTree(values)
    printBinarySearchTree(bst)

    print '\n'
    print '=== Binary Search Tree (Not Balanced) ==='

    values = [3, 5, 5, 7, 4, 1, 2]
    bst = createBinarySearchTreeNotBalanced(values)
    printBinarySearchTree(bst)

    print '\n'
    print '=== Complete Binary Search Tree ==='

    values = [1, 2, 3, 4, 5, 6, 7, 8]
    bst = createCompleteBinarySearchTree(values)
    printBinarySearchTree(bst)





