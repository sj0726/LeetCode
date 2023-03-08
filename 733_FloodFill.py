class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = image[sr][sc]
        coordinates = [(sr,sc)]
        def solve(sr, sc):
            image[sr][sc] = None # center
            if sr - 1 >= 0 and image[sr-1][sc] == original: # above
                coordinates.append((sr-1, sc))
                image[sr-1][sc] = None
                solve(sr-1, sc)
            if sr + 1 < len(image) and image[sr+1][sc] == original: # below
                coordinates.append((sr+1, sc))
                image[sr+1][sc] = None
                solve(sr+1, sc)
            if sc - 1 >= 0 and image[sr][sc-1] == original: # left
                coordinates.append((sr, sc-1))
                image[sr][sc-1] = None
                solve(sr, sc-1)
            if sc + 1 < len(image[0]) and image[sr][sc+1] == original: # right
                coordinates.append((sr, sc+1))
                image[sr][sc+1] = None
                solve(sr, sc+1)
        solve(sr, sc)
        for coord in coordinates:
            image[coord[0]][coord[1]] = color
        return image

print(Solution().floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0))