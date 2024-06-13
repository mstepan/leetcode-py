from medium.number_of_nodes_in_the_sub_tree_with_the_same_label import Solution
import pytest
import sys


class TestSolution:

    cur = Solution()

    def test_count_sub_trees1(self):
        assert self.cur.countSubTrees(
            7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd"
        ) == [
            2,
            1,
            1,
            1,
            1,
            1,
            1,
        ]

    def test_count_sub_trees2(self):
        assert self.cur.countSubTrees(4, [[0, 1], [1, 2], [0, 3]], "bbbb") == [
            4,
            2,
            1,
            1,
        ]

    def test_count_sub_trees3(self):
        assert self.cur.countSubTrees(5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab") == [
            3,
            2,
            1,
            1,
            1,
        ]

    def test_count_sub_trees_with_shuffled_edges(self):
        assert self.cur.countSubTrees(4, [[0, 2], [0, 3], [1, 2]], "aeed") == [
            1,
            1,
            2,
            1,
        ]

    def test_count_sub_trees_single_node(self):
        assert self.cur.countSubTrees(1, [], "a") == [1]

    def test_count_sub_trees_emty_tree(self):
        self.cur.countSubTrees(0, [], "") == []


if __name__ == "__main__":
    sys.exit(pytest.main())
