class Solution:
    """
    2952. Minimum Number of Coins to be Added
    https://leetcode.com/problems/minimum-number-of-coins-to-be-added/description/

    time: O(K*lgK), where K = max( target,  len(coins))
    space: O(1)
    """

    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        coins.sort()

        covered_boundary = 0
        added_elements_count = 0
        idx = 0

        while covered_boundary < target:
            if idx >= len(coins):
                covered_boundary += 1
                added_elements_count += 1
                covered_boundary = covered_boundary * 2 - 1
            else:
                if coins[idx] <= covered_boundary + 1:
                    covered_boundary += coins[idx]
                    idx += 1
                else:
                    covered_boundary += 1
                    added_elements_count += 1
                    covered_boundary = covered_boundary * 2 - 1

        return added_elements_count
