"""
LeetCode 704: Binary Search
https://leetcode.com/problems/binary-search/
"""


def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    # Typical case
    result1 = binary_search([-1, 0, 3, 5, 9, 12], 9)
    print("Test 1:", result1)
    assert result1 == 4

    # Edge case: single element, not found
    result2 = binary_search([5], 2)
    print("Test 2:", result2)
    assert result2 == -1

    # Edge case: empty array
    result3 = binary_search([], 1)
    print("Test 3:", result3)
    assert result3 == -1

    print("All tests passed.")
