import unittest

"""
1519. Number of Nodes in the Sub-Tree With the Same Label
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""


class Node:
    def __init__(self, index: int, label: chr):
        self.index = index
        self.label = label
        self.children = []

    def __str__(self):
        return f"{self.index}: {self.label}"


class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        if n == 0:
            return []
        if n == 1:
            return [1]

        all_nodes: list[Node] = [
            Node(idx, node_label) for idx, node_label in enumerate(labels)
        ]

        tree: Node = Solution.build_tree(all_nodes, edges)

        results = [0 for _ in range(n)]

        Solution.count_subtrees_rec(tree, results)

        return results

    @staticmethod
    def build_tree(all_nodes: list[Node], edges: list[list[int]]) -> Node:

        linked_nodes: set[int] = set()
        linked_nodes.add(0)

        for single_edge in edges:

            parent: Node = all_nodes[single_edge[0]]
            child: Node = all_nodes[single_edge[1]]

            if parent.index not in linked_nodes:
                parent, child = child, parent

            parent.children.append(child)

            linked_nodes.add(parent.index)
            linked_nodes.add(child.index)

        return all_nodes[0]

    @staticmethod
    def count_subtrees_rec(cur_node: Node, results: list[int]) -> dict[chr, int]:

        combined_labels = {cur_node.label: 1}

        for cur_child in cur_node.children:
            child_labels = Solution.count_subtrees_rec(cur_child, results)
            combined_labels = Solution.merge(combined_labels, child_labels)

        results[cur_node.index] = combined_labels[cur_node.label]

        return combined_labels

    @staticmethod
    def merge(first: dict[chr, int], second: dict[chr, int]) -> dict[chr, int]:
        combined = first.copy()

        for key, value in second.items():
            if key in combined:
                combined[key] += value
            else:
                combined[key] = value

        return combined


# ===============================================================
# TESTS
# ===============================================================
class TestSolution(unittest.TestCase):
    """
    Do post-order tree traversal (all children -> parent) and count unique labels using dictionary.
    time: O(N)
    space: O(h), could be O(N) in worst case
    """

    def test_count_sub_trees1(self):
        self.assertEquals(
            [2, 1, 1, 1, 1, 1, 1],
            Solution().countSubTrees(
                7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd"
            ),
        )

    def test_count_sub_trees2(self):
        self.assertEquals(
            [4, 2, 1, 1], Solution().countSubTrees(4, [[0, 1], [1, 2], [0, 3]], "bbbb")
        )

    def test_count_sub_trees3(self):
        self.assertEquals(
            [3, 2, 1, 1, 1],
            Solution().countSubTrees(5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab"),
        )

    def test_count_sub_trees_with_shuffled_edges(self):
        self.assertEquals(
            [1, 1, 2, 1], Solution().countSubTrees(4, [[0, 2], [0, 3], [1, 2]], "aeed")
        )

    def test_count_sub_trees_single_node(self):
        self.assertEquals([1], Solution().countSubTrees(1, [], "a"))

    def test_count_sub_trees_emty_tree(self):
        self.assertEquals([], Solution().countSubTrees(0, [], ""))


if __name__ == "__main__":
    unittest.main()
