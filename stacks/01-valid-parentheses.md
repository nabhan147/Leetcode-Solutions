## Problem: Valid Parentheses (Easy)

**Link:** https://leetcode.com/problems/valid-parentheses/

### Approach
Used a stack. Pushed every opening bracket. On a closing bracket,
popped the stack and checked it matches the corresponding opener via
a lookup dict. If the stack is empty when a closing bracket appears,
or a mismatch occurs, the string is invalid.

### Complexity
- Time: O(n)
- Space: O(n)

### Notes
The final `not stack` check matters — a string like "(()" passes all
individual bracket checks but leaves an unclosed "(" on the stack, so
it must still be rejected. Empty string is valid by definition (stack
stays empty throughout).
