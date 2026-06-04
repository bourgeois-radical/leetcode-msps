"""
200. Number of Islands - Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 0 = water
        # 1 = land

        # goal: count how many components of 1s connected horizontally or vertically exist in this grid?

        # lovely property: if I start at a cell of a component and visit everything "reachable" from it, we will visit
        # only the elements of that component and nothing else.

        def explore_island_dfs(
            grid: List[List[str]], cell_i: int, cell_j: int
        ) -> List[List[str]]:
            rows = len(grid)
            cols = len(grid[0])

            if cell_i < 0 or cell_i >= rows:
                raise ValueError("i-th element is out of grid's rows range")

            if cell_j < 0 or cell_j >= cols:
                raise ValueError("j-th element is out of grid's column range")

            directions = [
                ("up", -1, 0),
                ("down", 1, 0),
                ("right", 0, 1),
                ("left", 0, -1),
            ]

            # DFS = stack since stack is vertical: last in first out
            stack = deque()
            stack.append((cell_i, cell_j))
            grid[cell_i][cell_j] = "0"

            while stack:
                base_i, base_j = stack.pop()

                for _, move_i, move_j in directions:
                    neighbour_i = base_i + move_i
                    neighbour_j = base_j + move_j

                    if (neighbour_i >= 0 and neighbour_j >= 0) and (
                        neighbour_i < rows and neighbour_j < cols
                    ):
                        if grid[neighbour_i][neighbour_j] == "1":
                            stack.append((neighbour_i, neighbour_j))
                            grid[neighbour_i][neighbour_j] = "0"
                        else:
                            continue
                    else:
                        # print("The cell coordinates are not valid: neighbour_i = %s; neighbour_j = %s", neighbour_i, neighbour_j)
                        continue

            return grid

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        islands_counter = 0

        # step 1: go through the grid as if you are reading a book (for for loop)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    # step 2: if you have encountered a 1 that you have not visited yet -> increment the counter of islands
                    islands_counter += 1

                    # should we do it by copy or by reference?
                    # step 3: starting from the new 1 explore the entire island using DFS (Depth First Search)
                    grid = explore_island_dfs(grid=grid, cell_i=i, cell_j=j)

        return islands_counter

        # step 4: transfigure each 1 you visited into water (0)


if __name__ == "__main__":
    # Example 1 — should return 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    # Example 2 — should return 3
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    solution = Solution()
    print(solution.numIslands(grid=grid1))
    print(solution.numIslands(grid=grid2))
