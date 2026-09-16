"""
LeetCode 20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    # Typical case
    result1 = is_valid("()[]{}")
    print("Test 1:", result1)
    assert result1 is True

    # Edge case: mismatched closing bracket
    result2 = is_valid("(]")
    print("Test 2:", result2)
    assert result2 is False

    # Edge case: empty string
    result3 = is_valid("")
    print("Test 3:", result3)
    assert result3 is True

    print("All tests passed.")
