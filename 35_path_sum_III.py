import unittest
from typing import List, Optional
"""
Problem Understanding:
- Since Looking for a parth sum of the target number,
	- DFS would do the trick
		- key is to pass the array of all the current sum, and count


- so Time complexity will be O(n)
- space complexity would be O(n) or O(depth)

there is another approach:
we can have defaultdictionary storing the running count
look up in the dictionary to find [total-targetSum]
it should return either o or 1
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def dfs(self, node, sums: List, count: List, targetSum: int):
        if node:
            if node.val == targetSum:
                count[0] += 1

            for i in range(len(sums)):
                sums[i] += node.val
                if sums[i] == targetSum:
                    count[0] += 1

            sums.append(node.val)

            l_sums, r_sums = sums[:], sums[:]
            if node and node.left:
                self.dfs(node.left, l_sums, count, targetSum)
            if node and node.right:
                self.dfs(node.right, r_sums, count, targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        c = 1 if root.val == targetSum else 0
        sums, count = [root.val], [c]
        self.dfs(root.left, sums[:], count, targetSum)
        self.dfs(root.right, sums[:], count, targetSum)

        return count[0]
