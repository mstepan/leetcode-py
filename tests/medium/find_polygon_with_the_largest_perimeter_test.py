from leetcode.medium.find_polygon_with_the_largest_perimeter import Solution
import pytest
import sys


class TestSolution:
    cur = Solution()

    def test_largest_perimeter(self):
        assert self.cur.largestPerimeter([1, 12, 1, 2, 5, 50, 3]) == 12
        assert self.cur.largestPerimeter([5, 5, 5]) == 15
        assert self.cur.largestPerimeter([5, 5, 50]) == -1


if __name__ == "__main__":
    sys.exit(pytest.main())
