import unittest
"""
Problem understanding:
return the number of possible unique paths
using breath first search, take one position, add new direction
later realize that we can do that in dynamic programming. I was able to figure out the formula
dyanmic programming with tabular bottom up appraoch will get us the no. of paths


Solution Approach:
using tabular bottom up appraoch:
initialize a new grid m X n
set first row and column to 1s
loop through rest to add top and back column and row cells
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]

        for i in range(m):
            grid[i][0] = 1

        for j in range(n):
            grid[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

        return grid[-1][-1]
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_scenarios(self):
        self.assertEqual(self.sol.uniquePaths(3, 7), 28)
        self.assertEqual(self.sol.uniquePaths(3, 2), 3)

if __name__ == '__main__':
    unittest.main()
    