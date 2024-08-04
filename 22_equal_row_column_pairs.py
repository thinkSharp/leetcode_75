import unittest
from collections import Counter
from typing import List
"""
Problem understanding:
compare and Row pair with Column pair
if they are same increase the count:

Solution Approach:
- using zip to unzip the row pairs to column pairs
- save the row pair in count
- loop through the column pairs

Time Complexity: O(r) + O(c)
Space Complexity O(c) + O (r)
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column_pairs = list(zip(*grid))
        column_count = Counter(column_pairs)
        rows = [tuple(item) for item in grid]
        row_count = Counter(rows)
        count = 0
        for key, val in row_count.items():
            if key in column_count:
                count += val * column_count[key]
        return count
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]), 1)
        self.assertEqual(self.sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]), 3)


if __name__ == '__main__':
    unittest.main()