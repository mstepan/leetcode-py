"""
970. Powerful Integers
https://leetcode.com/problems/powerful-integers/description/
"""


class Solution:
    """
    K = log2(10^6) ~ 20
    time:  O(K^2)
    space: O(K)
    """

    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        left: list[int] = Solution.list_of_powers(x, bound)
        right: list[int] = Solution.list_of_powers(y, bound)

        res: set[int] = set()

        for val1 in left:
            for val2 in right:
                values_sum = val1 + val2

                if values_sum > bound:
                    break

                res.add(values_sum)

        return list(res)

    @staticmethod
    def list_of_powers(base_value: int, bound: int) -> list[int]:
        if base_value == 1:
            return [1]

        res: list[int] = []
        val = 1

        while val <= bound:
            res.append(val)
            val *= base_value

        return res
