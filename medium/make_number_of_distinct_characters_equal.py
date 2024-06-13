import unittest

"""
2531. Make Number of Distinct Characters Equal
https://leetcode.com/problems/make-number-of-distinct-characters-equal/
"""


class Solution:
    """
    N = len(word1 + word2)
    K = 26 (a..z chars)
    time: O(N*K^2)
    space: O(K)
    """

    def isItPossible(self, word1: str, word2: str) -> bool:
        Solution.check_not_none(word1, "'word1'")
        Solution.check_not_none(word2, "'word2'")

        freq1 = Solution.create_freq_table(word1)
        freq2 = Solution.create_freq_table(word2)

        if abs(len(freq1) - len(freq2)) > 2:
            return False

        bigger = freq1
        smaller = freq2

        if len(smaller) > len(bigger):
            bigger = freq2
            smaller = freq1

        list1 = [key for key in bigger.keys()]
        list2 = [key for key in smaller.keys()]

        for ch1 in list1:
            for ch2 in list2:
                Solution.swap(ch1, bigger, ch2, smaller)

                if len(bigger) == len(smaller):
                    return True

                Solution.swap(ch1, smaller, ch2, bigger)

        return False

    @staticmethod
    def swap(ch1: chr, freq1: dict[chr, int], ch2: chr, freq2: dict[chr, int]):
        Solution.dec_value(ch1, freq1)
        Solution.inc_value(ch2, freq1)

        Solution.dec_value(ch2, freq2)
        Solution.inc_value(ch1, freq2)

    @staticmethod
    def create_freq_table(value: str) -> dict[chr, int]:
        table = {}
        for ch in value:
            Solution.inc_value(ch, table)

        return table

    @staticmethod
    def inc_value(key: chr, table: dict[chr, int]):
        if key in table:
            table[key] += 1
        else:
            table[key] = 1

    @staticmethod
    def dec_value(key: chr, table: dict[chr, int]):
        if key in table:
            table[key] -= 1
            if table[key] == 0:
                del table[key]
        else:
            raise Exception(f"Can't find key = {key} in table {table}")

    @staticmethod
    def check_not_none(value: str, error_msg: str):
        if value is None:
            raise Exception(f"None value detected: {error_msg}")
