"""
Problem: Rotting Oranges

Intuition:
-----------
Each rotten orange spreads rot to its adjacent fresh oranges
(up, down, left, right) every minute.

This is a classic "multi-source BFS" problem:
- All rotten oranges are sources of infection.
- Rot spreads level by level (minute by minute).

So:
Minute 0 → initially rotten oranges
Minute 1 → neighbors rot
Minute 2 → their neighbors rot
... and so on

We simulate this using BFS.

Key idea:
Push ALL rotten oranges into queue initially.
Process layer-by-layer → each layer = 1 minute.

At the end:
If any fresh orange remains → return -1
Else → return total minutes taken
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Add all rotten oranges to queue
        # Count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # If no fresh oranges → no time needed
        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS
        while queue and fresh > 0:
            for _ in range(len(queue)):  # process one "minute"
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1
        

"""
Approach:
-----------
1. Treat all rotten oranges as BFS sources.
2. Spread rot level-by-level.
3. Each BFS level = 1 minute.
4. Stop when no fresh oranges remain.

Complexity:
-----------
Time  : O(rows * cols)
Space : O(rows * cols)  (queue in worst case)
"""
