import unittest

"""
1647. Minimum Deletions to Make Character Frequencies Unique
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""


class Solution:
    """
    Time: O(N*lgN)
    Space: O(N)
    """

    def minDeletions(self, s: str) -> int:
        freq_table: dict[chr, int] = Solution.calculate_chars_freq(s)

        values: list[int] = list(freq_table.values())

        if len(values) < 2:
            return 0

        values.sort(reverse=True)

        max_freq: int = values[0]
        del_cnt: int = 0

        for i in range(1, len(values)):
            max_freq = max(max_freq - 1, 0)
            freq = values[i]

            if freq >= max_freq:
                del_cnt += freq - max_freq
            else:
                max_freq = freq

        return del_cnt

    @staticmethod
    def calculate_chars_freq(s: str) -> dict[chr, int]:
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        return freq
