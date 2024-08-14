import unittest
from functools import cache
"""
This is easy solution: can be implemented multiple ways
1) recursion with using @cache decorator
2) recursion with memo
3) loop with memo dictionary
4) loop with memo list
"""
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
    
    def tribonacci_2(self, n: int) -> int:
        memo = [0, 1, 1]
        for i in range(3, n + 1):
            memo.append(memo[i - 3] + memo[i - 2], memo[i - 1])
        return memo[n]