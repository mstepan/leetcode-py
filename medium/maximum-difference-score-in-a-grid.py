import unittest


class Solution:
    """
    Use dynamic approach
    time: O(N*M * (N+M)), 10^5 * (1000 + 1000) = 200M
    space: O(N*M)
    """

    def maxScore(self, grid: list[list[int]]) -> int:
        if grid is None:
            raise Exception("grid is None")

        rows = len(grid)
        if rows == 0:
            return 0

        cols = len(grid[0])

        max_result = float("-inf")

        sol = [[0 for _ in row] for row in grid]

        for row in range(rows):
            for col in range(cols):

                if row == 0 and col == 0:
                    continue

                max_cur = float("-inf")

                # check all to the left, row wize
                for i in range(col):
                    max_cur = max(
                        max_cur, grid[row][col] - grid[row][i] + max(sol[row][i], 0)
                    )

                # check all to the top, column wize
                for i in range(row):
                    max_cur = max(
                        max_cur, grid[row][col] - grid[i][col] + max(sol[i][col], 0)
                    )

                sol[row][col] = max_cur
                max_result = max(max_result, max_cur)

        return max_result


# ===============================================================
# TESTS
# ===============================================================
class TestSolution(unittest.TestCase):

    def test_grid_positive_sum(self):
        grid = [[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]
        self.assertEquals(9, Solution().maxScore(grid))

    def test_grid_negative_sum(self):
        grid = [[4, 3, 2], [3, 2, 1]]
        self.assertEquals(-1, Solution().maxScore(grid))


if __name__ == "__main__":
    unittest.main()
