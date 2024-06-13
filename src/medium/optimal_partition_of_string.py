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
