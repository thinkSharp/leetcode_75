import unittest
from typing import List
"""
Problem understanding: 
	- find the contiguous subarray whose length is equal to K
	- get the max average
	
Solution approach
	max_avg = 0
	loop nums
		calculate the avarage
			compare and add the max
	
	return the max_avg
	
	
	Time Complexity: O(n)
	Space Complexity: O(1)
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k : int) -> float:
        max_sum = sum(nums[:k])
        curr_sum = max_sum
        for i in range(len(nums) -k):
            curr_sum = curr_sum - nums[i] + nums[i+k]
            max_sum = max(curr_sum, max_sum)
        return round(max_sum / k, 5)
    
    def findMaxAverage_avg(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        if k > len(nums):
            return max_avg
        elif k == 1:
            return max(nums)
        last_avg, first_num = sum(nums[0:k]) / k, nums[0]
        max_avg = max(max_avg, last_avg)
        for i in range(1, len(nums) + 1 - k):
            dif = (nums[i + k - 1] - first_num) / k
            last_avg = last_avg + dif
            max_avg = max(max_avg, last_avg)
            first_num = nums[i]
            
        return round(max_avg, 5)
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.findMaxAverage([1,12,-5,-6,50,3], 4), 12.7500)
        self.assertEqual(self.sol.findMaxAverage([5], 1), 5.0000)

    def test_failed_cases(self):
        self.assertEqual(self.sol.findMaxAverage([0,1,1,3,3],4), 2.00)
        self.assertEqual(self.sol.findMaxAverage([8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891],93), -594.58065)
        
if __name__ == '__main__':
    unittest.main()