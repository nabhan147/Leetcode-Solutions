## Problem: Reverse Linked List (Easy)

**Link:** https://leetcode.com/problems/reverse-linked-list/

### Approach
Iterative pointer-reversal: kept a `prev` pointer (starts as None) and
walked through the list one node at a time, flipping each node's
`next` pointer to point backward before advancing.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
A recursive solution is also common but uses O(n) call-stack space,
so the iterative version is the tighter choice. Included small helper
functions (`build_list`, `to_list`) to make local testing easier —
these aren't part of the LeetCode submission itself. Tested the
empty-list case (`head=None`), which correctly returns None.
