import unittest
from typing import List
from collections import defaultdict
"""
Problem Understanding:
there are 0 to n-1 cities and n-1 road => other words, if 6 cities then 5 roads
find the minimum number of road that need to change the direction?

Solution Approach:
flip_count = 0
destination set() => 0
loop through edges:
	if y in destination set:
		add x to destination set
  else x in destination set:
		flip+cout += 1
		add x in destination set
		
	return flip_count
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        curr = seen = {0}
        count = 0
        for c in connections:
            adj[c[0]].append(c)
            adj[c[1]].append(c)

        
        while curr:
            new = set()
            for v in curr:
                for e in adj[v]:
                    if e[0] not in seen and e[1] == v:
                        new.add(e[0])
                    elif e[0] == v and e[1] not in seen:
                        new.add(e[1])
                        count += 1
            curr = new
            seen.update(new)
        
        return count
    

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.minReorder(3,[[1,0],[2,0]]), 0)
        self.assertEqual(self.sol.minReorder(3, [[1,0],[2,0]]), 0)


if __name__ == '__main__':
    unittest.main()