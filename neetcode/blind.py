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

    # Sum of two integer
    def getSum(self, a: int, b: int) -> int:
        s = a ^ b
        c = a & b
        while c != 0:
            c = c << 1
            new_s = s ^ c
            c = s & c
            s = new_s

        return s

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]

    def canJump(self, nums: List[int]) -> bool:
        m = nums[0]
        for i in range(0, len(nums)):
            if i > m:
                break

            m = max(m, nums[i] + i)
            if m >= len(nums) - 1:
                return True

        return False

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0

        print(matrix, first_row_zero)

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        return
