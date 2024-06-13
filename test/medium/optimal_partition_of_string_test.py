from medium.optimal_partition_of_string import Solution
import pytest
import sys


class TestSolution:

    cur = Solution()

    def test_partition_string(self):
        assert self.cur.partitionString("abacaba") == 4
        assert self.cur.partitionString("abc") == 1
        assert self.cur.partitionString("aaa") == 3
        assert self.cur.partitionString("b") == 1

    def test_partition_empty_string(self):
        assert self.cur.partitionString("") == 0

    def test_partition_none_string_should_fail(self):
        with pytest.raises(Exception) as context:
            self.cur.partitionString(None)

        assert str(context.value) == "None 's' detected"


if __name__ == "__main__":
    sys.exit(pytest.main())
