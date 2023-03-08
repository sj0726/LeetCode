class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def bfs(i, j):
            grid[i][j] = "-1" # marking it visited
            queue = [(i,j)]
            while queue:
                x = queue.pop(0)
                row = x[0]
                col = x[1]
                if row + 1 < len(grid) and grid[row+1][col] == "1": # bottom
                    queue.append((row+1, col))
                    grid[row+1][col] = "-1"
                if col + 1 < len(grid[0]) and grid[row][col+1] == "1": # right
                    queue.append((row, col+1))
                    grid[row][col+1] = "-1"
                if row - 1 >= 0 and grid[row-1][col] == "1": # above
                    queue.append((row-1, col))
                    grid[row-1][col] = "-1"
                if col - 1 >= 0 and grid[row][col-1] == "1": # left
                    queue.append((row, col-1))
                    grid[row][col-1] = "-1"


        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1": # land, unvisited
                    count += 1
                    bfs(i, j)
        return count
    
print(Solution().numIslands(grid =
[
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
))