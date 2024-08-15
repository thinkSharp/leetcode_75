import unittest
from typing import List
"""
Problem Understanding:
- Get Maximum profit from buy and selling stocks at the right time
- at least one price point, fee can be zero

Solution Approach:
- solve this wtih recursion, dynamic programming top down, tabular bottom up

Time complexity will be O(n)
Space complexity will be O(n) as well since we will be saving in 
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        def dp(idx, action):
            if idx == n:
                return 0
            if action == 'b':
                buy = -prices[idx] + dp(idx + 1, 's')
                not_buy = dp(idx + 1, 'b')
                return max(buy, not_buy)
            else:
                sell = prices[idx] - fee + dp(idx + 1, 'b')
                not_sell = dp(idx + 1, 's')
                return max(sell, not_sell)
        return dp(0, 'b')
    
    def maxProfit_memo(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = [[-1] * 2 for _ in range(n)]
        def dp(idx, action):
            if idx == n:
                return 0
            if memo[idx][action] == -1:
                if action:
                    buy = -prices[idx] + dp(idx + 1, False)
                    not_buy = dp(idx + 1, True)
                    memo[idx][action] = max(buy, not_buy)
                else:
                    sell = prices[idx] - fee + dp(idx + 1, True)
                    not_sell = dp(idx + 1, False)
                    memo[idx][action] = max(sell, not_sell)
            return memo[idx][action]
        
        return dp(0, True)
                
            


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self. sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.maxProfit(prices = [1,3,2,8,4,9], fee = 2), 8)
        self.assertEqual(self.sol.maxProfit(prices = [1,3,7,5,10,3], fee = 3), 6)

    def test_given_cases_memo(self):
        self.assertEqual(self.sol.maxProfit_memo(prices = [1,3,2,8,4,9], fee = 2), 8)
        self.assertEqual(self.sol.maxProfit_memo(prices = [1,3,7,5,10,3], fee = 3), 6)


if __name__ == '__main__':
    unittest.main()


