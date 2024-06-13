from medium.minimum_deletions_to_make_character_frequencies_unique import Solution

import pytest
import sys


class TestSolution:

    cur = Solution()

    def test_min_deletions_with_zero_deletion(self):
        assert self.cur.minDeletions("aab") == 0

    def test_min_deletions_typical_case(self):
        assert self.cur.minDeletions("aaabbbcc") == 2
        assert self.cur.minDeletions("ceabaacb") == 2

    def test_min_deletions_tricky_case(self):
        assert self.cur.minDeletions("bbcebab") == 2


if __name__ == "__main__":
    sys.exit(pytest.main())
