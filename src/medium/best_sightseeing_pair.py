import unittest

"""
1014. Best Sightseeing Pair
https://leetcode.com/problems/best-sightseeing-pair/description/
"""


class Solution:
    """
    Use dynamic-like approach, similar to Kadane's algorithm
    time: O(N)
    space: O(1)
    """

    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        if len(values) < 2:
            return 0

        max_score: int = 0
        max_left: int = values[0]

        for i in range(1, len(values)):
            max_left -= 1
            max_score = max(max_score, max_left + values[i])

            if values[i] > max_left:
                max_left = values[i]

        return max_score
