import unittest
from collections import deque
from typing import List
"""
Problem Understanding:
- Finding the nearest exit from starting point
- if starting point is the exist, ignore that
- ++++ are represented as wall
- . . . . are represented as path

Solution Approach:
- BFS will do the trick
- First initialize the queue and visited node
- add the start position.
- create a functon to traverse 4 direction (up, down, left, right) => return only directions that can be traverse.
- once out, check if this is exist, if not and not visited add them in queue and move on


time complexity and space complexity are O(n * m)
"""
class Solution:
    def getNeighbors(self, maze: List[List[str]], position: List[int]) -> List[List[int]]:
        result = []
        n = len(maze)
        m = len(maze[0])

        up = (position[0] - 1, position[1])
        down = (position[0] + 1, position[1])
        left = (position[0], position[1] - 1)
        right = (position[0], position[1] + 1)

        if up[0] < 0 or maze[up[0]][up[1]] != '+':
            result.append(up) 
        if down[0] >= n or maze[down[0]][down[1]] != '+':
            result.append(down)
        if left[1] < 0 or maze[left[0]][left[1]] != '+':
            result.append(left)
        if right[1] >= m or maze[right[0]][right[1]] != '+':
            result.append(right)

        return result

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        queue = deque()
        visited = set()
        entrance = tuple(entrance)
        queue.append((entrance, 0))
        while queue:
            path, count = queue.popleft()
            neighbors = self.getNeighbors(maze, path)

            for p in neighbors:
                if p not in visited:
                    visited.add(p)
                    if  ((p[0] < 0 or p[0] >= n) or (p[1] < 0 or p[1] >= m)):
                        if path != entrance:
                            return count
                    else:
                        queue.append((p, count + 1))
        return -1
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.nearestExit([["."],["."],["."],["."]], [2,0]), 1)
        self.assertEqual(self.sol.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]), 1)
        self.assertEqual(self.sol.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]), 2)
        self.assertEqual(self.sol.nearestExit([[".","+"]], [0,0]), -1)

if __name__ == '__main__':
    unittest.main()