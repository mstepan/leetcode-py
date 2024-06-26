from hard.number_of_beautiful_integers_in_the_range import Solution
import pytest
import sys


class TestSolution:
    cur = Solution()

    def test_number_of_beautiful_integers1(self):
        assert self.cur.numberOfBeautifulIntegers(10, 20, 3) == 2

    def test_number_of_beautiful_integers2(self):
        assert self.cur.numberOfBeautifulIntegers(36, 60, 3) == 3

    def test_number_of_beautiful_integers_big_range(self):
        assert self.cur.numberOfBeautifulIntegers(349_863_935, 772_153_463, 11) == 0


if __name__ == "__main__":
    sys.exit(pytest.main())
