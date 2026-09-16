"""
LeetCode 155: Min Stack
https://leetcode.com/problems/min-stack/
(Substituted for the topic's second stack problem, same difficulty band.)
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # tracks running minimum at each level

    def push(self, val):
        self.stack.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    # Typical case
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print("Test 1 (min):", ms.get_min())
    assert ms.get_min() == -3
    ms.pop()
    print("Test 1 (top):", ms.top())
    assert ms.top() == 0
    print("Test 1 (min after pop):", ms.get_min())
    assert ms.get_min() == -2

    # Edge case: single element
    ms2 = MinStack()
    ms2.push(5)
    print("Test 2:", ms2.get_min(), ms2.top())
    assert ms2.get_min() == 5 and ms2.top() == 5

    print("All tests passed.")
