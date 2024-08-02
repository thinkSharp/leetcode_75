import unittest
from typing import List
"""
Understanding the Problem; 
- finding the biggest container
	- height is the value of the index
	- width is the difference between two indexes

Solution Approach:
	two pointers
		- left = 0, right is len(n)
		= max_w = 0
		while left < right:
			height = min(left, right)
			width = right - left
			area = height * width
			max_w = max(max_w, area)
			if left < right:
				left ++
			else:
				right --
			else:
				left ++
				right --
			return max_w
			
			Time complexity: O(n)
			Space Complexity : O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_w = 0
        left, right = 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            a = h * w
            max_w = max(max_w, a)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_w
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(self.sol.maxArea([1,1]),1)

if __name__ == '__main__':
    unittest.main()
