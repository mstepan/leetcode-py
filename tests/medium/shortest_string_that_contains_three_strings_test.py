from leetcode.medium.shortest_string_that_contains_three_strings import Solution
import pytest
import sys


class TestSolution:
    cur = Solution()

    def test_shortest_string1(self):
        assert self.cur.minimumString("abc", "bca", "aaa") == "aaabca"

    def test_shortest_string2(self):
        assert self.cur.minimumString("ab", "ba", "aba") == "aba"

    def test_shortest_string3(self):
        assert self.cur.minimumString("cab", "a", "b") == "cab"


if __name__ == "__main__":
    sys.exit(pytest.main())
