import unittest
"""
Problem understanding:
1) check if two strings are close using following two operations:
	  - rearrange any word
	  - or transfrom every occurance with one of the existing character


Solution approach:
- check the length different return False
- second check the set, if same then return true
- check the char count. they should be the same 

Time Complexity: O(nlogn) for sorting the count, it could be n in worst case
Space Complexity O(n) for creating sets and array
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        w1_count = [word1.count(ch) for ch in set(word1)]
        w2_count = [word2.count(ch) for ch in set(word2)]
        w1_count.sort()
        w2_count.sort()
        if w1_count != w2_count:
            return False
            
        return True
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.closeStrings('abc', 'bca'), True)
        self.assertEqual(self.sol.closeStrings('a', 'aa'), False)
        self.assertEqual(self.sol.closeStrings('cabbba','abbccc'), True)
        self.assertEqual(self.sol.closeStrings('abbzzca','babzzcz'), False)

if __name__ == '__main__':
    unittest.main()