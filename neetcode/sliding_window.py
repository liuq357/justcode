from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        dip = prices[0]
        profit = 0
        for p in prices:
            profit = max(profit, p - dip)
            if p < dip:
                dip = p

        return profit

    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        for r in range(0, len(s)):
            if s[r] == " ":
                char_set = set()
                continue

            while s[r] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[r])
            max_len = max(max_len, len(char_set))

        return max_len

    @staticmethod
    def character_replacement(s: str, k: int) -> int:
        count = {}

        left = 0
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            if (r - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

        return len(s) - left

    @staticmethod
    def check_inclusion(s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        for s in s1:
            s1_count[ord(s) - ord('a')] += 1

        s2_sub = [0] * 26
        for l in range(len(s2)):
            s2_sub[ord(s2[l]) - ord('a')] += 1
            if l - len(s1) >= 0:
                s2_sub[ord(s2[l - len(s1)]) - ord('a')] -= 1

            if tuple(s1_count) == tuple(s2_sub):
                return True

        return False

    @staticmethod
    def min_window(s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        got, need = 0, len(count_t)
        l, sub_str = 0, ""
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in count_t and window[c] == count_t[c]:
                got += 1

            while got == need:
                sub_str = s[l: r + 1] if sub_str == "" or r + 1 - l < len(sub_str) else sub_str
                c = s[l]
                window[c] -= 1
                if c in count_t and window[c] < count_t[c]:
                    got -= 1
                l += 1

        return sub_str
