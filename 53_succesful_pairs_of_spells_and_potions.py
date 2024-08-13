import unittest
from typing import List
"""
Problem Understanding:
find the successful pairs of spells and positions 
- condition if product is greater then success

Solution approach:
 we could sort the position:
	 start calculating from (perform binary search and perform from mid)
	 if spell is 1 then just compare value with success
	 
	
Time complexity wost case O(mlogn)
space complexity O(m)
"""
class Solution:
    def binarySearch(self, nums: List[int], spell: int, success: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            s = nums[mid] * spell
            if s < success:
                left = mid + 1
            elif s >= success:
                right = mid - 1
                

        return n - left

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        for spell in spells:
            count = self.binarySearch(potions, spell, success)
            result.append(count)
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_failed_cases(self):
        self.assertEqual(self.sol.binarySearch([1,2,3,4,5,6,7], 4, 25), 1)

    def test_given_cases_binary_search(self):
        self.assertEqual(self.sol.binarySearch([5,8,8], 3, 16), 2)
        self.assertEqual(self.sol.binarySearch([5,8,8], 1, 16), 0)
        self.assertEqual(self.sol.binarySearch([5,8,8], 2, 16), 2)
        self.assertEqual(self.sol.binarySearch([1,2,3,4,5], 1, 7), 0)
        self.assertEqual(self.sol.binarySearch([1,2,3,4,5], 5, 7), 4)
        self.assertEqual(self.sol.binarySearch([1,2,3,4,5], 3, 7), 3)

    def test_given_cases(self):
        self.assertEqual(self.sol.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7), [4,0,3])
        self.assertEqual(self.sol.successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16), [2,0,2])



if __name__ == '__main__':
    unittest.main()
