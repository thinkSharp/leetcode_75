import unittest
from typing import Optional
"""
Problem understanding:
   finding the zigzag from the binary tree
	 dfs can assist
		 important is how to find the maximum zz
			 always need the direction it comes from:
				 exmple: if left then child node should be
								 left, count = 1
								 right count += 1
								 max(left, right)
								 
								 return max
								 
								 
				Time complexity : O(n)
				Space Complexity: O(n)
				
"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def dfs(self, node: TreeNode, direction: str, max_val: int) -> int:
        if not node:
            return 0
        l_max = 1 if direction == 'l' else max_val + 1
        r_max = 1 if direction == 'r' else max_val + 1
        return max(max_val, self.dfs(node.left, 'l', l_max), self.dfs(node.right, 'r', r_max))

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.dfs(root.left, 'l', 1), self.dfs(root.right, 'r', 1))