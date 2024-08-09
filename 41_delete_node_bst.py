import unittest
from typing import Optional
"""
problem Understanding:
- Delete a Node from BST
- First search the Node:
- Once found, replace with left node if exist else right now. 
		- adjust their left and right nodes
		- if no leaf nodes, simply delete this node by removing the link from parents
	- creating three functions:
		- search function
		- find largest node
		- delete function
			- delete the largest leaf node
			- repalce current node with largest node value


- Solution approach:
	- search_bst:
		- loop through curr .val:
			- if matches return node
			- otherwise, move left or right according to the value
- find largest:
	- from the tree, look for largest from right side first
	- if no right side, look at left:
	- 
- Delete_node:
	- replace sub root node with largest node
	- if largest node has children 
	- rearrange the links
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def getMinNode(self, node: Optional[TreeNode]) ->Optional[TreeNode]:
            curr = node
            while curr and curr.left:
                 if curr.left:
                      curr = curr.left
                
            return curr
    

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
             return root

        if key < root.val:
             root.left = self.deleteNode(root.left, key)
        elif key > root.val:
             root.right = self.deleteNode(root.right, key)
        else:
             #found 
             # Check if it has one branch
             if not root.left:
                  return root.right
             elif not root.right:
                  return root.left

             temp = self.getMinNode(root.right)

             root.val = temp.val

             root.right = self.deleteNode(root.right, temp.val)
        return root
        
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def get_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(7)

        return root
    
    def get_tree_result(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(7)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)


        return root
    
    def test_given_cases(self):
        root = self.get_tree()
        result = self.get_tree_result()
        deleted = self.sol.deleteNode(root, 6)
        self.assertEqual(result, result)


if __name__ == '__main__':
    unittest.main()
