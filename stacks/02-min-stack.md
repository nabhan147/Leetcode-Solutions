## Problem: Min Stack (Medium)

**Link:** https://leetcode.com/problems/min-stack/

### Approach
Used two parallel stacks: the main data stack, and a second stack
that tracks the minimum value seen at each level. Every push records
the min of the new value and the previous minimum, so `get_min()` is
always just the top of the second stack.

### Complexity
- Time: O(1) for push, pop, top, and get_min
- Space: O(n)

### Notes
The naive approach of scanning the whole stack for the minimum on
each `get_min()` call is O(n) per call. The parallel min-stack trades
extra space for O(1) lookups, which is the whole point of the
problem. Tested with a single-element stack to confirm push/get_min
behave correctly before any pop happens.
