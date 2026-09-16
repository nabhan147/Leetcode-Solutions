"""
LeetCode 206: Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    # Typical case
    head1 = build_list([1, 2, 3, 4, 5])
    result1 = to_list(reverse_list(head1))
    print("Test 1:", result1)
    assert result1 == [5, 4, 3, 2, 1]

    # Edge case: single node
    head2 = build_list([1])
    result2 = to_list(reverse_list(head2))
    print("Test 2:", result2)
    assert result2 == [1]

    # Edge case: empty list
    result3 = to_list(reverse_list(None))
    print("Test 3:", result3)
    assert result3 == []

    print("All tests passed.")
