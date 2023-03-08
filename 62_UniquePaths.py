class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        # creates a 2D matrix with first row and column filled with 1
        # because first row (0, j) and column (i, 0) means they're only approachable from 1 direction only (trivial)
        # path[i][j] = the number of possible paths to reach to (i, j)
        # path[i][j] = # of paths to reach the block to the left (i-1, j) + # of paths to reach the block above (i, j-1)
        # because from the block to the left or above, there's only 1 way of reaching (i, j): either move right once, or move down once
        path = [[1 for j in range(cols)] for i in range(rows)]

        # and we use DP to start from the beginning, ignoring the trivial cases
        for i in range(1, rows):
            for j in range(1, cols):
                path[i][j] = path[i-1][j] + path[i][j-1]
        
        return path[m-1][n-1]
        

print(Solution().uniquePaths(3, 7))