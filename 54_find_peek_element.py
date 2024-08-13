import unittest
from typing import List
"""
Problem Understanding:
- find Peak Element
	- Peak element is an emement that both left and right elements are less then itself
	- must be done in O(logn)
	- both positive and negative nums.


Solution approach:
left, right 
mid 
	if mid-1 < mid > mid + 1:
		return mind
	elif mid < mid + 1:
		left = mid
	else:
		right = mid
"""
class Solution:
    def binarySearch(self, nums: List[int], n: int, left: int, right: int) -> int:
    
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if mid - 1 >= 0 and mid + 1 <= n - 1:
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
        elif mid == 0 and mid + 1 <= n - 1:
            if nums[mid] > nums[mid + 1]:
                return mid
        elif mid == n - 1:
            if nums[mid] > nums[mid -1]:
                return mid
        
        left_mid =  self.binarySearch(nums, n, left, mid - 1)
            
        right_mid =  self.binarySearch(nums, n, mid + 1, right)

        return left_mid if left_mid >= 0 else right_mid

    def findPeakElement1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        left, right = 0, n
        return self.binarySearch(nums, n, left, right)
    
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 2:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1

        l, r = 1, n - 2

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.findPeakElement([3,2,1]), 0)
        self.assertEqual(self.sol.findPeakElement([1,2]), 1)
        self.assertEqual(self.sol.findPeakElement([1,2,3,4]), 3)
        self.assertEqual(self.sol.findPeakElement([1,2,3,1]), 2)
        self.assertEqual(self.sol.findPeakElement([1,2,1,3,4,5]), 1)
        self.assertEqual(self.sol.findPeakElement([1,2,1,3,5,6,4]), 1)


if __name__ == '__main__':
    unittest.main()


            