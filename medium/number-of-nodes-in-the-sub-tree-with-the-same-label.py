import unittest

"""
1519. Number of Nodes in the Sub-Tree With the Same Label
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""


class Node:
    def __init__(self, index: int, label: chr):
        self.index = index
        self.label = label
        self.left = None
        self.right = None

    def get_index(self):
        return self.index

    def get_label(self):
        return self.label

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def __str__(self):
        return f"{self.index}: {self.label}"


class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        if n == 0:
            return []
        if n == 1:
            return [1]

        all_nodes: list[Node] = [Node(idx, node_label) for idx, node_label in enumerate(labels)]

        tree: Node = Solution.build_tree(all_nodes, edges)

        results = [0 for _ in range(n)]

        Solution.count_subtrees_rec(tree, results)

        return results

    @staticmethod
    def build_tree(all_nodes: list[Node], edges: list[list[int]]) -> Node:

        for single_edge in edges:
            parent: Node = all_nodes[single_edge[0]]
            child: Node = all_nodes[single_edge[1]]

            if parent.get_left() is None:
                parent.set_left(child)
            else:
                parent.set_right(child)

        return all_nodes[0]

    @staticmethod
    def count_subtrees_rec(cur_node: Node, results: list[int]) -> dict[chr, int]:
        left_labels = {}
        if cur_node.get_left() is not None:
            left_labels = Solution.count_subtrees_rec(cur_node.get_left(), results)

        right_labels = {}
        if cur_node.get_right() is not None:
            right_labels = Solution.count_subtrees_rec(cur_node.get_right(), results)

        cur_idx: int = cur_node.get_index()
        cur_label: chr = cur_node.get_label()

        combined_labels = Solution.merge(left_labels, right_labels, cur_label)

        results[cur_idx] = combined_labels[cur_label]

        return combined_labels

    @staticmethod
    def merge(left: dict[chr, int], right: dict[chr, int], cur_label: chr) -> dict[chr, int]:
        combined = left.copy()

        for key, value in right.items():
            if key in combined:
                combined[key] += value
            else:
                combined[key] = value

        if cur_label in combined:
            combined[cur_label] += 1
        else:
            combined[cur_label] = 1

        return combined


# ===============================================================
# TESTS
# ===============================================================
class TestSolution(unittest.TestCase):
    """
    Do post-order tree traversal (left-right-parent) and count unique labels using set.
    time: O(N)
    space: O(h), could be O(N) in worst case
    """

    def test_count_sub_trees1(self):
        self.assertEquals([2, 1, 1, 1, 1, 1, 1],
                          Solution().countSubTrees(7,
                                                   [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                                                   "abaedcd"))

    def test_count_sub_trees2(self):
        self.assertEquals([4, 2, 1, 1],
                          Solution().countSubTrees(4,
                                                   [[0, 1], [1, 2], [0, 3]],
                                                   "bbbb"))

    def test_count_sub_trees3(self):
        self.assertEquals([3, 2, 1, 1, 1],
                          Solution().countSubTrees(5,
                                                   [[0, 1], [0, 2], [1, 3], [0, 4]],
                                                   "aabab"))

    def test_count_sub_trees_single_node(self):
        self.assertEquals([1], Solution().countSubTrees(1, [], "a"))

    def test_count_sub_trees_emty_tree(self):
        self.assertEquals([], Solution().countSubTrees(0, [], ""))


if __name__ == "__main__":
    unittest.main()
