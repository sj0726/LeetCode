class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[-1][-1] == 1:
            return 0
        # 1 is an obstacle
        row = len(obstacleGrid)
        column = len(obstacleGrid[0])
        table = [[0 for _ in range(column + 1)] for _ in range(row + 1)] # to accomodate for things like (6, 0)
        table[0][1] = 1 # could be table[1][0] too. either works.

        for i in range(1, len(table)):
            for j in range(1, len(table[0])):
                if not obstacleGrid[i-1][j-1]: # if the current cell isn't an obstacle
                    table[i][j] = table[i-1][j] + table [i][j-1]
        
        return table[-1][-1]


print(Solution().uniquePathsWithObstacles([[0,0]]))