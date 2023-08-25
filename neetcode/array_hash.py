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
