# 8.2 Reverse an linked list
from util import *


def reverse(head):
    if not head or not head.next:
        return head

    right = reverse(head.next)
    head.next.next = head
    head.next = None
    return right


def reverse_i(head):
    # p, q, head
    if not head or not head.next:
        return
    # printLinkedList(head)
    p = head
    q = head.next
    head.next = None
    head = q.next
    # printLinkedList(q)
    while head:
        q.next = p
        p, q, head = q, head, head.next
    q.next = p
    return q

# 8.2 Reverse Between m, n








if __name__ == '__main__':
    print "reverse linked list iterative and recursive"
    values = [1, 3, 5, 7, 9]
    ll = createLinkedList(values)
    ll = createLinkedList(values, rand=True, uni=True, size=5)
    printLinkedList(ll)
    ls = reverse(ll)
    printLinkedList(ls)
    ls = reverse_i(ls)
    printLinkedList(ls)
