from medium.best_sightseeing_pair import Solution
import pytest
import sys


class TestSolution:

    cur = Solution()

    def test_max_score_sightseeing_pair(self):
        assert self.cur.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
        assert self.cur.maxScoreSightseeingPair([1, 2]) == 2

    def test_max_score_sightseeing_pair_single_element_array(self):
        assert self.cur.maxScoreSightseeingPair([1]) == 0

    def test_max_score_sightseeing_pair_empty_array(self):
        assert self.cur.maxScoreSightseeingPair([]) == 0


if __name__ == "__main__":
    sys.exit(pytest.main())
