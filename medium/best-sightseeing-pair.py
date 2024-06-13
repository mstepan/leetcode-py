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


# ===============================================================
# TESTS
# ===============================================================
class TestSolution(unittest.TestCase):
    def test_max_score_sightseeing_pair(self):
        self.assertEquals(11, Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))
        self.assertEquals(2, Solution().maxScoreSightseeingPair([1, 2]))

    def test_max_score_sightseeing_pair_single_element_array(self):
        self.assertEquals(0, Solution().maxScoreSightseeingPair([1]))

    def test_max_score_sightseeing_pair_empty_array(self):
        self.assertEquals(0, Solution().maxScoreSightseeingPair([]))


if __name__ == "__main__":
    unittest.main()
