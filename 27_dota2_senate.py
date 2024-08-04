import unittest
"""
Predict which party announce victory

Example: RDRDRD => R
RDDDRR => R
DDDRRRR => R
DRDRD => D
DDRRR => 

Solution Approach:
prepare two queues:
one for R and one for D
start = snator[0]
voting round:
	loop through sentence and apply voting rule
	

Time Complexity O(n)
Space Complexity 1

"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = [], []
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        i = len(senate)
        while r and d:
            rp = r.pop(0)
            dp = d.pop(0)
            if rp  < dp:
                r.append(i)
            else:
                d.append(i)
            i += 1

                    
        if r:
            return 'Radiant'
        if d:
            return 'Dire'
        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.predictPartyVictory('RD'), 'Radiant')
        self.assertEqual(self.sol.predictPartyVictory('RDD'), 'Dire')
        self.assertEqual(self.sol.predictPartyVictory('DRRD'), 'Dire')
        self.assertEqual(self.sol.predictPartyVictory('RRDDDD'),'Dire')

if __name__ == '__main__':
    unittest.main()