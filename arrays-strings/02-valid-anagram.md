## Problem: Valid Anagram (Easy)

**Link:** https://leetcode.com/problems/valid-anagram/

### Approach
An early length check filters out obvious mismatches for free. Then
used `collections.Counter` to build a frequency map of characters for
each string and compared the two maps directly.

### Complexity
- Time: O(n)
- Space: O(n)

### Notes
Sorting both strings and comparing (`sorted(s) == sorted(t)`) also
works but costs O(n log n). The Counter approach is a cleaner O(n)
alternative. Handled the empty-string edge case, which trivially
returns True since both Counters are empty.
