import unittest
from collections import deque
from typing import List
"""
Problem Understanding:
- find the minimum no. of minutes that require to rot all oranges
- grid will have at least 1 row and column
- 0 is empty
- 1 is fresh
- 2 is rotten


Solution Approach:
- BFS to find the minimum no. of minutes
- traverse 4 direction, only pick up fresh oranges slots
- return if none left or -1 
- count the 1s and 2s. 
	- counting 1s will allow us to know if any fresh left after all possible tervasal 
	- we will also need the position of the first rotten orange

Space and time comlexity is O(n * m)
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque()
        minutes = 0
        fresh_count = 0
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        rotten = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        queue.append(rotten)
        while queue:
            rot = queue.popleft()
            rott = 0
            new_rotten = []
            for r in rot:
                p = [0, 0]
                for d in dir:
                    p[0] = r[0] + d[0]
                    p[1] = r[1] + d[1]

                    if (p[0] < 0 or p[0] >= n) or (p[1] < 0 or p[1] >= m):
                        continue
                    if grid[p[0]][p[1]] == 1:
                        grid[p[0]][p[1]] = 2
                        rott += 1
                        new_rotten.append((p[0], p[1]))
            if rott > 0:
                minutes += 1
                fresh_count -= rott
                queue.append(new_rotten)

        return minutes if fresh_count == 0 else -1
    

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)
        self.assertEqual(self.sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)
        self.assertEqual(self.sol.orangesRotting([[0,2]]), 0)
        self.assertEqual(self.sol.orangesRotting([[2,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,2]]), 3)
        self.assertEqual(self.sol.orangesRotting([[2,1,1],[1,1,1],[1,1,1]]), 4)


if __name__ == '__main__':
    unittest.main()