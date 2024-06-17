from medium.powerful_integers import Solution
import pytest
import sys


class TestSolution:
    cur = Solution()

    def test_normal_case1(self):
        assert self.cur.powerfulIntegers(2, 3, 10) == [2, 3, 4, 5, 7, 9, 10]

    def test_normal_case2(self):
        assert self.cur.powerfulIntegers(3, 5, 15) == [2, 4, 6, 8, 10, 14]


if __name__ == "__main__":
    sys.exit(pytest.main())
