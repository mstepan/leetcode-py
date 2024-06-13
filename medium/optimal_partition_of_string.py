import unittest

"""
2405. Optimal Partition of String
https://leetcode.com/problems/optimal-partition-of-string/description/
"""


class Solution:
    """
    Use greedy approach to construct optimal string partitions.
    time: (N)
    space: O(26) ~ O(1)
    """

    def partitionString(self, s: str) -> int:
        if s is None:
            raise Exception("None 's' detected")

        if len(s) == 0:
            return 0

        cnt: int = 1
        unique: set[chr] = set()

        for ch in s:
            if ch in unique:
                cnt += 1
                unique.clear()

            unique.add(ch)

        return cnt


# ===============================================================
# TESTS
# ===============================================================
class TestSolution(unittest.TestCase):
    def test_partition_string(self):
        self.assertEqual(4, Solution().partitionString("abacaba"))
        self.assertEqual(1, Solution().partitionString("abc"))
        self.assertEqual(3, Solution().partitionString("aaa"))
        self.assertEqual(1, Solution().partitionString("b"))

    def test_partition_empty_string(self):
        self.assertEqual(0, Solution().partitionString(""))

    def test_partition_None_string_should_fail(self):
        with self.assertRaises(Exception) as context:
            Solution().partitionString(None)
        self.assertTrue("None 's' detected", context.exception)


if __name__ == "__main__":
    if __name__ == "__main__":
        unittest.main()
