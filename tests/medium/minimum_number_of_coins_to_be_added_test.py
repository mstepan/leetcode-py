import sys

import pytest

from leetcode.medium.minimum_number_of_coins_to_be_added import Solution


class TestSolution:
    cur = Solution()

    def test_case1(self):
        assert self.cur.minimumAddedCoins([1, 4, 10], 19) == 2

    def test_case2(self):
        assert self.cur.minimumAddedCoins([1, 4, 10, 5, 7, 19], 19) == 1

    def test_case3(self):
        assert self.cur.minimumAddedCoins([1, 1, 1], 20) == 3


if __name__ == "__main__":
    sys.exit(pytest.main())
