"""
LeetCode 283: Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""


def move_zeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums


if __name__ == "__main__":
    # Typical case
    result1 = move_zeroes([0, 1, 0, 3, 12])
    print("Test 1:", result1)
    assert result1 == [1, 3, 12, 0, 0]

    # Edge case: no zeroes
    result2 = move_zeroes([1, 2, 3])
    print("Test 2:", result2)
    assert result2 == [1, 2, 3]

    # Edge case: all zeroes
    result3 = move_zeroes([0, 0, 0])
    print("Test 3:", result3)
    assert result3 == [0, 0, 0]

    print("All tests passed.")
