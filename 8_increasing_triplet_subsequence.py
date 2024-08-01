import unittest
from typing import List
"""
Problem Understanding: Find a triplet subsequence such that i < j  < k and num[i] < num[j] < num[k]

Solution Approach: creating a stack: which hold the triplet:
Example walk through: [1,2,3,4,5] => 
Loop through the list:
	check stack is empty append
	or check the last element with the current element,
		if the condition meet, num[i] > stack[-1]
				append to stack
		else:
			pop the stack and check till the last one
			
	 check the stack size
			 if 3 exist, then return True
			 
	return False
	
	
	Time Complexity; O(n) looping through the list once
	Space Complexity: O(3) Stack size which is constant
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        first, second = float('inf'), float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False
    
    def increasingTriplet_bad(self, nums: List[int]) -> bool:
        ln = len(nums)
        if ln < 2:
            return False
        ls = [nums[0]]
        rs = []
        for i in range(1,ln):
            if nums[i] > ls[-1]:
                ls.append(nums[i])
            elif len(ls) == 2 and nums[i] > ls[-2]:
                ls.pop()
                ls.append(nums[i])
            else:
                while rs and rs[-1] > nums[i]:
                    rs.pop()
                if rs and nums[i] > rs[-1] or not rs:
                    rs.append(nums[i])
            if len(rs) == 2:
                ls = rs
                rs = []
            if len(ls) == 3:
                return True

        return False

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.increasingTriplet([1,0,0,1]), False)
        self.assertEqual(self.sol.increasingTriplet([1,1,-2,6]), False)
        self.assertEqual(self.sol.increasingTriplet([1,5,0,4,1,3]), True)
        self.assertEqual(self.sol.increasingTriplet([20, 100, 10, 12, 5, 13]), True)
        self.assertEqual(self.sol.increasingTriplet([2,4,-2,-3]), False)
        self.assertEqual(self.sol.increasingTriplet([1,2,3,4,5]), True)
        self.assertEqual(self.sol.increasingTriplet([5,4,3,2,1]), False)
        self.assertEqual(self.sol.increasingTriplet([2,1,5,0,4,6]), True)


if __name__ == '__main__':
    unittest.main()

