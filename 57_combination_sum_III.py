import unittest
from typing import List
"""
Problem Understanding:
	find all valid combination of k numbers that sum up to n such that
	- only numbers 1 through 9 are used
	- each number is used at most once
	- if I am building all combination
		- loop through each digit K times:
				starting with 1:
						visited set()
						temp = []
						for j till 1 to k:
							if j not visited:
							 if j == k-1:
								 sum(temp) + j == n
								else
								sum(temp) + j < n
									temp.append(j)
									visited.add(j)
						 sum(temp) == n
							 add in final result
			Time complexity: O(k^9)						
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        stack = [frozenset({digits[i]}) for i in range(len(digits) -1, -1, -1) if digits[i] < n]
        visited = set()

        while stack:
            item = stack.pop()
            if item in visited:
                continue
            sum_c = sum(item)

            for d in digits:
                if d in item:
                    continue
                if len(item) + 1 == k and sum_c + d == n:
                    c = item | frozenset([d])
                    if c not in visited:
                        visited.add(c)
                        result.append(list(c))
                elif sum_c + d < n:
                    c = item | frozenset([d])
                    if c not in visited:
                        stack.append(c)
        return result
    
    def combinationSum3Optimized(self, k:int, n: int) -> List[List[int]]:
        current, result = [], []
        def helper(current, digits, target):
            if len(current) == k and target == 0:
                result.append(current)
                return
            if target < 0 or len(digits) == 0 or len(current) > k:
                return
            for i in range(len(digits)):
                helper(current=current + [digits[i]], digits=digits[i + 1:], target=target - digits[i])
        
        helper(current, [1, 2, 3, 4, 5, 6, 7 ,8, 9], n)
        return result
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases_optimized(self):
        self.assertEqual(self.sol.combinationSum3Optimized(3, 7), [[1,2,4]])
        self.assertEqual(self.sol.combinationSum3Optimized(3, 9), [[1,2,6],[1,3,5],[2,3,4]])
        self.assertEqual(self.sol.combinationSum3Optimized(2, 2), [])
        self.assertEqual(self.sol.combinationSum3Optimized(4, 2), [])

    def test_given_cases(self):
        self.assertEqual(self.sol.combinationSum3(3, 7), [[1,2,4]])
        self.assertEqual(self.sol.combinationSum3(3, 9), [[1,2,6],[1,3,5],[2,3,4]])
        self.assertEqual(self.sol.combinationSum3(2, 2), [])
        self.assertEqual(self.sol.combinationSum3(4, 2), [])


if __name__ == '__main__':
    unittest.main()