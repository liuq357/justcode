from typing import List


class Solution:
    @staticmethod
    def is_palindrome(s: str):
        h = 0
        t = len(s) - 1
        while h < t:
            while not s[h].isalnum() and h < t:
                h += 1
            while not s[t].isalnum() and h < t:
                t -= 1
            if s[h].lower() != s[t].lower():
                return False

            h += 1
            t -= 1

        return True

    @staticmethod
    def two_sum(numbers: List[int], target: int) -> List[int]:
        h, t = 0, len(numbers) - 1
        while h < t:
            if numbers[h] + numbers[t] < target:
                h += 1
            elif numbers[h] + numbers[t] > target:
                t -= 1
            else:
                return [h + 1, t + 1]

        return []

    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            if nums[i] > 0:
                break

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return res
