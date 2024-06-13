from medium.make_number_of_distinct_characters_equal import Solution

import pytest
import sys


class TestSolution:

    cur = Solution()

    def test_is_it_possible(self):
        assert self.cur.isItPossible("abcde", "fghij")


if __name__ == "__main__":
    sys.exit(pytest.main())
