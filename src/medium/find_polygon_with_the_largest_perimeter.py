"""
2971. Find Polygon With the Largest Perimeter
https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
"""


class Solution:
    """
    time: O(N*lgN)
    space: O(1)
    """

    def largestPerimeter(self, nums: list[int]) -> int:
        if nums is None:
            raise ValueError("None 'nums' detected")

        if len(nums) < 3:
            return -1

        nums.sort()

        perimeter_sum: int = 0
        max_perimeter: int = -1

        for i in range(len(nums)):
            elems_cnt = (i - 0) + 1

            if elems_cnt > 2 and perimeter_sum > nums[i]:
                max_perimeter = perimeter_sum + nums[i]

            perimeter_sum += nums[i]

        return max_perimeter
