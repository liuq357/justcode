from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        while head < tail:
            while not s[head].isalnum() and head < tail:
                head += 1
            while not s[tail].isalnum() and tail > head:
                tail -= 1

            if s[head].lower() != s[tail].lower():
                return False

            head += 1
            tail -= 1

        return True

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        i = 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    result.append([nums[i], nums[j], nums[k]])

                if s <= 0:
                    j += 1
                    while j < len(nums) - 1 and nums[j] == nums[j - 1]:
                        j += 1

                if s >= 0:
                    k -= 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1

            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return result
