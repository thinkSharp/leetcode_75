import unittest
"""
remove start and left char from the string. Left char must be non-start char

solution approach:
- convert string to list
- loop through the list
	- if star is found:
		- remove left of start and star itself
			- decrease the i


Time complexity O(len of s)
Space complexity O(n) 
"""
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
                
        return ''.join(stack)
    
class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.removeStars('leet**cod*e'), 'lecoe')
        self.assertEqual(self.sol.removeStars('erase*****'), '')


if __name__ == '__main__':
    unittest.main()
