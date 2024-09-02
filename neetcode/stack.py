from typing import List
from collections import deque


class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        if s == "":
            return False

        stack = deque()
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                continue

            if len(stack) == 0:
                return False

            if (c == ')' and stack.pop() != '(') or \
                    (c == '}' and stack.pop() != '{') or \
                    (c == ']' and stack.pop() != '['):
                return False

        return len(stack) == 0
