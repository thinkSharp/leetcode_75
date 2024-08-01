import unittest
import re
"""
Problem Understanding:
- Given a string reverse the words. Strips the extra white spaces around 
- return string should only contain single whilte space between words

Solutioin Approach
- Replace all the whilte spaces with single white space
- strip first and back spaces
- split string to get all the words
- loop through to reverse them

Time Complexity O(n) -> regex loop
space complexity O(n)
"""
class Solution:
    def reverseWords(self, s:str) -> str:
        s_clean = s.strip().split()
        s_clean_r = s_clean[::-1]
        return ' '.join(s_clean_r)
    
    def reverseWords_worst(self, s: str) -> str:
        cleaned_s = re.sub(r'\s+', ' ', s)
        cleaned_s = cleaned_s.strip()
        words = cleaned_s.split()
        first = 0
        last = len(words) - 1
        while first < last:
            words[first], words[last] = words[last], words[first]
            first += 1
            last -= 1
        return ' '.join(words)
    

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.reverseWords('the sky is blue'), 'blue is sky the')
        self.assertEqual(self.sol.reverseWords('     hello    world   '), 'world hello')


if __name__ == '__main__':
    unittest.main()