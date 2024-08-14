import unittest
from typing import List
"""
Problem understanding:
calculate min cost for climbing stairs
we can either climb one step or two by paying the cost or current step
base step can be either one or two

calculate based step first,
then loop through to find the next step till reach the top
	
Solution Approach:
i = 0, totoal = 0

while i < n:
two contidition:

	i, total = i+1, total + c[i +1] if c[i+1] < c[i+2] else i+2
last element:
	jump
	
return total:
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        memo = [-1] * n
        def dp(cost: List[int], n: int):
            if memo[n] != -1:
                return memo[n]

            if n == 0 or n == 1:
                memo[n] = cost[n]
            else:
                memo[n] = cost[n] + min(dp(cost, n - 1), dp(cost, n - 2))
            
            return memo[n]

        return min(dp(cost, n - 1), dp(cost, n - 2))
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_given_cases(self):
        self.assertEqual(self.sol.minCostClimbingStairs([10,15,20]), 15)
        self.assertEqual(self.sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]), 6)

if __name__ == '__main__':
    unittest.main()

