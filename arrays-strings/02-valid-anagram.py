"""
LeetCode 242: Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""

from collections import Counter


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    # Typical case
    result1 = is_anagram("anagram", "nagaram")
    print("Test 1:", result1)
    assert result1 is True

    # Edge case: different lengths
    result2 = is_anagram("rat", "car")
    print("Test 2:", result2)
    assert result2 is False

    # Edge case: empty strings
    result3 = is_anagram("", "")
    print("Test 3:", result3)
    assert result3 is True

    print("All tests passed.")
