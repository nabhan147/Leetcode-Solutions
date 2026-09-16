"""
LeetCode 1: Two Sum
https://leetcode.com/problems/two-sum/
"""


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    # Typical case
    result1 = two_sum([2, 7, 11, 15], 9)
    print("Test 1:", result1)
    assert result1 == [0, 1], f"Expected [0, 1], got {result1}"

    # Edge case: duplicates in array
    result2 = two_sum([3, 3], 6)
    print("Test 2:", result2)
    assert result2 == [0, 1], f"Expected [0, 1], got {result2}"

    print("All tests passed.")
