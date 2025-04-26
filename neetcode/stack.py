from typing import List
from collections import deque


class MinStack:
    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min or self._min[-1] > val:
            self._min.append(val)
        else:
            self._min.append(self._min[-1])

    def pop(self) -> None:
        self._stack.pop()
        self._min.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[-1]


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

    def eval_RPN(self, tokens: List[str]) -> int:
        ops = []
        for t in tokens:
            print(ops, "-->", t)
            if t == "+":
                ops.append(ops.pop() + ops.pop())
            elif t == "-":
                ops.append(-ops.pop() + ops.pop())
            elif t == "*":
                ops.append(ops.pop() * ops.pop())
            elif t == "/":
                a = ops.pop()
                b = ops.pop()
                ops.append(int(b / a))
            else:
                ops.append(int(t))

        return ops.pop()
