"""
Problem understanding: Lowest common ancestor of a binary tree. 
- find the lowest common ancestor of two nodes
- a node to be a descendant of itself

Solution Approach:
dfs that collects all the ancestors . when found for P and Q, stop and loop through one of the list to compare.

dfs(node, p, q)
	based condition
	  check node is none, or node is p or node is q
			return node
			
		left_lca = dfs(root.left, p, q)
		right_lca = dfs(root.right, p, q)
		
		if left and right:
			return root
			
		return left if left or return right
"""
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca else right_lca