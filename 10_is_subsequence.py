import unittest
"""
understanding Problem:  What is the asked?
  - find the subsequence by removing if necessary but wihtout changing the relative position of each char

Solution Approach:
found_index = 0
 loop the substring:
	 loop the main string from found_index till len(n):
		 compare sub with main char:
				 if found:
					 found_index = j + 1
					 break
				if j == len(n) - 1 and i < len(n) - 1:
					return False
					
		return True
		
		
		Time Complexity: O(s + t)
		Space Complexity O(1)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)

        if ls == lt == 1 or ls == lt:
            return True if s == t else False
        
        found = 0
        for i in range(len(s)):
            for j in range(found, len(t)):
                if s[i] == t[j]:
                    found = j + 1
                    break
                if j == len(t) - 1 and i != len(s) - 1:
                    return False
        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.isSubsequence('abc', 'ahbgdc'), True)
        self.assertEqual(self.sol.isSubsequence('axc', 'ahbgdc'), False)

    def test_failed_cases(self):
        self.assertEqual(self.sol.isSubsequence('a','c'), False)


if __name__ == '__main__':
    unittest.main()