import unittest
"""
Problem Understanding: For a given string, find the max vowels of size k sub string. 
S consists of lower case, s length is at least 1 and 10^5
K could be as big as S

Example: abcdeaeioudefgj, K = 5 

Pseudo Code:
max_v = 0
vowels = 'aeiou'
max_v = sum(i for i in s[:k] if i in vowels)
curr = max_v
for i in range(1, len(s) - k):
	curr += -1 if s[i]  in vowels else 0
	curr += 1 if s[i+k] in vowels else 0
	max_v = max(max_v, curr)
return max_v

Time Complexity:  O(n) len of S
Space Complexity: O(1)

"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_v = sum(1 for i in s[:k] if i in vowels)
        curr = max_v
        for i in range(len(s) - k):
            curr += -1 if s[i] in vowels else 0
            curr += 1 if s[i + k] in vowels else 0
            if curr > max_v:
                max_v = curr
        return max_v
    

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.maxVowels('abciiide', k = 3), 3)
        self.assertEqual(self.sol.maxVowels('aeiou', 2), 2)
        self.assertEqual(self.sol.maxVowels('leetcode', 3), 2)

    def test_failed_cases(self):
        self.assertEqual(self.sol.maxVowels('weallloveyou',7), 4)


if __name__ == '__main__':
    unittest.main()

