## Problem: Merge Two Sorted Lists (Easy)

**Link:** https://leetcode.com/problems/merge-two-sorted-lists/

### Approach
Used a dummy head node to simplify edge handling, then walked both
lists simultaneously with a `tail` pointer, always attaching the
smaller of the two current nodes. Once one list runs out, the
remainder of the other list is attached directly since it's already
sorted.

### Complexity
- Time: O(n + m)
- Space: O(1) (reuses existing nodes, no new list allocated)

### Notes
The dummy-node trick avoids special-casing "what if the very first
node comparison determines the head" — a pattern worth reusing in
other list-merging problems. Tested with one list empty and both
lists empty to confirm no null-pointer errors.
