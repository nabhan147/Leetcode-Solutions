## Problem: Two Sum (Easy)

**Link:** https://leetcode.com/problems/two-sum/

### Approach
Used a single-pass hash map to store each number's index as we iterate.
For every element, check whether its complement (target - num) has
already been seen; if so, we've found the pair immediately without a
nested loop.

### Complexity
- Time: O(n)
- Space: O(n)

### Notes
The naive brute-force approach is O(n²) with nested loops. Storing
seen values in a dict trades space for time and turns the lookup into
O(1) on average. Duplicate values (e.g. [3, 3] with target 6) work
correctly because we check for the complement before inserting the
current number.
