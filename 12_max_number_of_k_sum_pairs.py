import unittest
from collections import defaultdict
from typing import List
"""
Problem Understanding:
- for a given K,
- if sum(2) matches with K then remove and count ++
- loop through till no more and return count

Solution Approach:
create  a default dictionary of num to list of index
	loop through nums:
		for a given i see if (k -i) in the dict:
				if true:
					count += 1
					remove both i and (k-i) from dict
		return count
		
		
	Time Complexity: O(n)
	space Complexity O(n) for dictionary
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_map = defaultdict(list)
        count = 0
        for i in range(len(nums)):
            nums_map[nums[i]].append(i)
        for i in range(len(nums)):
            if nums[i] == (k - nums[i]) and len(nums_map[nums[i]]) >= 2:
                count += 1
                nums_map[nums[i]].pop()
                nums_map[nums[i]].pop()
            elif nums[i] != (k - nums[i]) and len(nums_map[nums[i]]) > 0 and len(nums_map[k - nums[i]]) > 0:
                count += 1
                nums_map[nums[i]].pop()
                nums_map[k - nums[i]].pop()
        return count
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.maxOperations([1,2,3,4], 5), 2)
        self.assertEqual(self.sol.maxOperations([3,1,3,4,3], 6), 1)


if __name__ == '__main__':
    unittest.main()