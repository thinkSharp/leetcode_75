import unittest
from typing import List
"""
Problem understanding:
- Move all zeros while maintaining the relative order of non-zero element
- must be in-place (meaning no copy of array)

Example: 0, 1, 0, 3, 12
i = 0, check if non zero:
	continue
else:
	find first non zero index j (store J as global variable so that we can loop from there next time
	swap

Solution Approach:

j = 1
loop through i through n:
	if i == 0:
		while j < n: 
			if num[j] != 0:
				swap
				j++
				break
			j++
			
			
Time complexity: O(n + n) => 2n so O(n)
space is O(1) inplace swap
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        checked = 0
        while i < len(nums) and checked < len(nums) - 1:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
            checked += 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_given_cases(self):
        nums = [0,0,1]
        self.sol.moveZeroes(nums)
        self.assertEqual(nums, [1,0,0])

        nums = [0,1,0,3,12]
        self.sol.moveZeroes(nums)
        self.assertEqual(nums, [1,3,12,0,0])

if __name__ == '__main__':
    unittest.main()

