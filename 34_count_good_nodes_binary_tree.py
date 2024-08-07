import unittest
from typing import List
"""
Problem Understanding:
- count the good nodes, 
	- Definition: good nodes are those node, if the path form root to X there are no nodes which value greater then X

Solution Approach:
- create DFS that would count the good nodes
	- having running max arry, running count arry to store the values
	
	Time and Space complexity is O(n)
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def dfs(self, node: TreeNode, largest: List, count: List):
        if node and node.val >= largest[0]:
            count[0] += 1
            largest[0] = node.val

        l_largest, r_largest = largest[:], largest[:]
        if node and node.left:
            self.dfs(node.left, l_largest, count)

        if node and node.right:
            self.dfs(node.right, r_largest, count)

    def goodNodes(self, root: TreeNode) -> int:
        left_largest, right_largest, count = [root.val], [root.val], [1]

        self.dfs(root.left, left_largest, count)
        self.dfs(root.right, right_largest, count)

        return count[0]
