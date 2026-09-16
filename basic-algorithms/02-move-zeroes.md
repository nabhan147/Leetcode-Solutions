## Problem: Move Zeroes (Easy)

**Link:** https://leetcode.com/problems/move-zeroes/

### Approach
Used a two-pointer / "insert position" technique. Walked through the
array with index `i`; whenever a non-zero value is found, it's
swapped into `insert_pos` and the pointer advances. This keeps all
non-zero elements in their original relative order while pushing
zeroes to the end, done in place.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
Swapping instead of just overwriting avoids needing a separate pass
to fill trailing zeroes. Tested the all-zero and no-zero edge cases
to confirm the array is left unchanged where nothing needs to move.
