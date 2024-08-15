import unittest
from typing import List
"""
Problem Understanding: rob maximum money without getting caught
- adjacent houses will get you caught

Solution Apporach:
- [2,1,1,2, 1,2,1,1,2,1,1,2,1,2,2,1] => 
for recursive programming with db:
    base case if i > len
        return 0
    if memo[i] return memo
    memo[i] = max(nums[i] + dp(i+2), dp(i))
    return memo[i]

for i (2, n):

"""
class Solution:
    def rob_tabular(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        if nums[1] < nums[0] : nums[1] = nums[0]

        for i in range(2, n):
            nums[i] = max(nums[i-1], nums[i] + nums[i - 2])
        return nums[-1]
    
    def rob_recursive(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def dp(i, n):
            if i >= n:
                return 0
            if memo[i] == -1:
                memo[i] = max(nums[i] + dp(i + 2, n), dp(i + 1, n))

            return memo[i]
        
        return dp(0, n)
    

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases_tabular(self):
        self.assertEqual(self.sol.rob_tabular([2, 1, 1, 2]), 4)
        self.assertEqual(self.sol.rob_tabular([1, 2]), 2)
        self.assertEqual(self.sol.rob_tabular([1, 2, 3, 1, 5, 4, 3, 2, 1, 1, 1, 1, 4, 3, 5, 6, 7]), 30)
        self.assertEqual(self.sol.rob_tabular([2, 7, 9, 3, 1]), 12)
        self.assertEqual(self.sol.rob_tabular([1,2,3,1]), 4)

    def test_given_cases_recursive(self):
        self.assertEqual(self.sol.rob_recursive([2, 1, 1, 2]), 4)
        self.assertEqual(self.sol.rob_recursive([1, 2]), 2)
        self.assertEqual(self.sol.rob_recursive([1, 2, 3, 1, 5, 4, 3, 2, 1, 1, 1, 1, 4, 3, 5, 6, 7]), 30)
        self.assertEqual(self.sol.rob_recursive([2, 7, 9, 3, 1]), 12)
        self.assertEqual(self.sol.rob_recursive([1,2,3,1]), 4)

if __name__ == '__main__':
    unittest.main()
