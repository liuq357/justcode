import collections
import heapq
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def contain_duplicate(nums: List[int]) -> bool:
        s = set()
        for v in nums:
            if v in s:
                return True
            else:
                s.add(v)

        return False

    @classmethod
    def quick_sort(cls, nums: List[int], low, high: int):
        if low < high:
            i = cls.q_sort_partition(nums, low, high)
            cls.quick_sort(nums, low, i - 1)
            cls.quick_sort(nums, i + 1, high)

    @classmethod
    def q_sort_partition(cls, nums: List[int], low, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = 26 * [0]
        for c in s:
            count[ord(c) - 97] += 1

        for c in t:
            if count[ord(c) - 97] == 0:
                return False
            count[ord(c) - 97] -= 1

        return True

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_n = sorted(nums)

        head = 0
        tail = len(nums) - 1
        found = False
        while head < tail:
            total = sorted_n[head] + sorted_n[tail]
            if total == target:
                found = True
                break
            elif total < target:
                head += 1
            else:
                tail -= 1

        if not found:
            return [-1, -1]

        a_idx = b_idx = -1
        for i in range(len(nums)):
            if nums[i] == sorted_n[head] and a_idx == -1:
                a_idx = i
            elif nums[i] == sorted_n[tail]:
                b_idx = i

        return [a_idx, b_idx]

    @staticmethod
    def two_integer_sum(nums, target):
        prev_map = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in prev_map:
                return [prev_map[need], i]
            else:
                prev_map[nums[i]] = i

        return []

    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return [v for v in res.values()]

    @staticmethod
    def top_k_frequent(nums, k):
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        freq = [[] for i in range(1 + len(nums))]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            if len(freq[i]) > 0:
                res.extend(freq[i])
                k -= len(freq[i])
            if k <= 0:
                return res

        return res

    @staticmethod
    def product_except_self(nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums), 1):
            result[i] = result[i - 1] * nums[i - 1]

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * temp
            temp *= nums[i]

        return result

    @staticmethod
    def encode(strs: List[str]) -> str:
        # number of char and a '$' sign followed by string.
        delimiter = "$"
        res = ""
        for s in strs:
            count = len(s)
            res += str(count) + delimiter + s

        return res

    @staticmethod
    def decode(s: str) -> List[str]:
        res = []
        while len(s) > 0:
            idx = s.find('$')
            count = int(s[:idx])
            res.append(s[idx + 1:idx + 1 + count])
            s = s[idx + count + 1:]

        return res

    @staticmethod
    def is_valid_sudoku(board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num_str = board[r][c]
                if num_str == ".":
                    continue

                num = int(num_str)
                if num in rows[r] or num in columns[c] or num in boxes[(r // 3, c // 3)]:
                    return False

                rows[r].add(num)
                columns[c].add(num)
                boxes[(r // 3, c // 3)].add(num)

        return True

    @staticmethod
    def longest_consecutive(nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums:
            # check whether n is the starting number of a consecutive sequence
            if (n - 1) not in s:
                length = 0
                while (n + length) in s:
                    length += 1

                longest = max(longest, length)

        return longest
