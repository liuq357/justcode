import collections
import heapq
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return Solution.contains_duplicate2(nums, 0, len(nums) - 1)

    @staticmethod
    def containsDuplicate2(nums: List[int]) -> bool:
        nums_dict = {}
        for v in nums:
            if v in nums_dict:
                return True
            nums_dict[v] = 0

        return False

    @staticmethod
    def contains_duplicate2(nums: List[int], low, high: int) -> bool:
        if low < high:
            duplicated, pi = Solution.duplicate_partition(nums, low, high)
            if duplicated:
                return True

            if Solution.contains_duplicate2(nums, low, pi - 1):
                return True
            if Solution.contains_duplicate2(nums, pi + 1, high):
                return True

        return False

    @staticmethod
    def duplicate_partition(nums: List[int], low, high: int) -> (bool, int):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] == pivot:
                return True, i + 1

            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return False, i + 1

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

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        m = {}
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1

        for c in t:
            if m.get(c, 0) == 0:
                return False
            m[c] -= 1

        return True

    def isAnagram2(self, s: str, t: str) -> bool:
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            group_strs = word_map.get(sorted_s, [])
            group_strs.append(s)
            word_map[sorted_s] = group_strs

        result = []
        for group_strs in word_map.values():
            result.append(group_strs)

        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        top_k = [0] * k
        heapq.heapify(top_k)
        for count in count_map.values():
            heapq.heappush(top_k, count)
            heapq.heappop(top_k)

        result = []
        k_small = heapq.heappop(top_k)
        for num, count in count_map.items():
            if count >= k_small:
                result.append(num)

        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums) - 1):
            res[i] = nums[i] * res[i - 1]

        print(res)

        p = 1
        for j in range(len(nums) - 1, 0, -1):
            res[j] = p * res[j - 1]
            p *= nums[j]

        res[0] = p

        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid row
        for r in board:
            slots = [0] * 10
            for num_str in r:
                if num_str == ".":
                    continue

                slots[int(num_str)] += 1
                if slots[int(num_str)] > 1:
                    return False

        # valid column
        for c in range(0, 9):
            slots = [0] * 10
            for r in range(0, 9):
                num_str = board[r][c]
                if num_str == ".":
                    continue
                slots[int(num_str)] += 1
                if slots[int(num_str)] > 1:
                    return False

        # valid sub-boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                slots = [0] * 10
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        num_str = board[i][j]
                        print(f'{i}.{j}->{num_str}')
                        if num_str == ".":
                            continue
                        slots[int(num_str)] += 1
                        if slots[int(num_str)] > 1:
                            return False

        return True

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
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

    def longestConsecutive(self, nums: List[int]) -> int:
        processed = set()
        head_tail = {}
        tail_head = {}
        for num in nums:
            if num in processed:
                continue

            print("=>", num)

            extended = False
            # extend head_tail
            if num + 1 in head_tail:
                extended = True
                tail = head_tail.pop(num + 1)
                head_tail[num] = tail
                tail_head[tail] = num

            # extend tail_head
            if num - 1 in tail_head:
                extended = True
                head = tail_head.pop(num - 1)
                tail_head[num] = head
                head_tail[head] = num

            # merge
            if extended and num in head_tail and num in tail_head:
                head_tail[tail_head[num]] = head_tail[num]
                tail_head[head_tail[num]] = tail_head[num]
                head_tail.pop(num)
                tail_head.pop(num)

            # no extend and merge
            if not extended:
                head_tail[num] = num
                tail_head[num] = num

            processed.add(num)

        res = 0
        for h, t in head_tail.items():
            if t - h + 1 > res:
                res = t - h + 1

        return res

