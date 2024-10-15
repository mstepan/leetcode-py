from leetcode.medium.maximum_difference_score_in_a_grid import Solution

import pytest
import sys


class TestSolution:

    cur = Solution()

    def test_grid_positive_sum(self):
        grid = [[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]
        assert self.cur.maxScore(grid) == 9

    def test_grid_negative_sum(self):
        grid = [[4, 3, 2], [3, 2, 1]]
        assert self.cur.maxScore(grid) == -1


if __name__ == "__main__":
    sys.exit(pytest.main())
