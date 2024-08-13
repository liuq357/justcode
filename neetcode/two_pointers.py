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

    @staticmethod
    def max_area(heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        m_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            m_area = max(m_area, area)
            if heights[l] <= heights[r]:
                j = l + 1
                while j < r and heights[j] <= heights[l]:
                    j += 1
                l = j
            else:
                k = r - 1
                while l < k and heights[k] <= heights[r]:
                    k -= 1
                r = k

        return m_area

    @staticmethod
    def trap(height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            if height[left] <= height[right]:
                j = left + 1
                while j < right and height[j] <= height[left]:
                    area += height[left] - height[j]
                    j += 1
                left = j
            else:
                k = right - 1
                while left < k and height[k] <= height[right]:
                    area += height[right] - height[k]
                    k -= 1
                right = k

        return area
