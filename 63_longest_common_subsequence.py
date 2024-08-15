import unittest
"""
Problem Understanding:
finding longest common subsequence:
ace
abcde
idea is to use dynamic programming tabular approach

grid = initialized with 0 for len of two strings
add extra row plus extra column
in order to adjust, add two char to the existing text
for i (1 to n)
	for j ( 1 to m
		if text[i] == text[j];
				get the grid[i-1][j-1] + 1
		else:
			get max(grid[i-1][j], grid[i][j-1])
			
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m , n = len(text1) + 1, len(text2) + 1
        t1 = '-' + text1
        t2 = '.' + text2
        grid = [[0] * n for _ in range(m)]
        
        for i in range(m):
            grid[i][0] = 0
        for j in range(n):
            grid[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if t1[i] == t2[j]:
                    grid[i][j] = 1 + grid[i - 1][j - 1]
                else:
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.longestCommonSubsequence('abcde', 'ace'), 3)
        self.assertEqual(self.sol.longestCommonSubsequence('abc', 'abc'), 3)
        self.assertEqual(self.sol.longestCommonSubsequence('abc', 'def'), 0)
        self.assertEqual(self.sol.longestCommonSubsequence('abcde', 'cda'), 2)


if __name__ == '__main__':
    unittest.main()