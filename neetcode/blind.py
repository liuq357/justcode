from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sum = c_sum = nums[0]
        for num in nums[1:]:
            if c_sum < 0:
                if c_sum < num:
                    c_sum = num
            else:
                if num < 0 and m_sum < c_sum:
                    m_sum = c_sum
                if c_sum + num < 0:
                    c_sum = 0
                else:
                    c_sum += num

        if m_sum < c_sum:
            m_sum = c_sum

        return m_sum
