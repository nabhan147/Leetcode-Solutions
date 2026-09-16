"""
LeetCode 21: Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
(Substituted for the topic's second linked-list problem, same difficulty band.)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next


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
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    result1 = to_list(merge_two_lists(l1, l2))
    print("Test 1:", result1)
    assert result1 == [1, 1, 2, 3, 4, 4]

    # Edge case: one empty list
    l3 = build_list([])
    l4 = build_list([0])
    result2 = to_list(merge_two_lists(l3, l4))
    print("Test 2:", result2)
    assert result2 == [0]

    # Edge case: both empty
    result3 = to_list(merge_two_lists(None, None))
    print("Test 3:", result3)
    assert result3 == []

    print("All tests passed.")
