import unittest
from typing import List
"""
Problem Understanding:
- have set of rooms and set of keys in each room.
- Find out if all rooms can be visited

Solution Approach:
- define a set for the key since we can use it to open all rooms
- remove used key
- continue till the end of the rooms or exist out if key doesn't exist
- according to the discussion, room can be visited out of order
	- therefore changing the implementation
		- creating a room set,
		- remove them if visited 
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        keys, visited = set(), set()
        keys = keys.union(set(rooms[0]))
        visited.add(0)
        while keys:
            key = keys.pop()
            if key not in visited:
                visited.add(key)
                keys |= set(rooms[key])
        return len(visited) == len(rooms)
    

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_given_cases(self):
        self.assertEqual(self.sol.canVisitAllRooms([[1],[2],[3],[]]), True)
        self.assertEqual(self.sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]), False)
        self.assertEqual(self.sol.canVisitAllRooms([[2],[],[1]]), True)

if __name__ == '__main__':
    unittest.main()
