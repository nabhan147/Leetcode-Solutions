## Problem: Binary Search (Easy)

**Link:** https://leetcode.com/problems/binary-search/

### Approach
Standard iterative binary search on a sorted array. Maintained `lo`
and `hi` pointers, checked the midpoint each round, and narrowed the
range based on whether the midpoint value was too low or too high.

### Complexity
- Time: O(log n)
- Space: O(1)

### Notes
Used iteration instead of recursion to keep space O(1) — a recursive
version would add O(log n) call-stack space. Tested the empty-array
edge case separately since `lo > hi` immediately on an empty list,
which correctly short-circuits to -1.
