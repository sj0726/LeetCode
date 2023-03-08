class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        You must write a solution in O(log(m * n)) time complexity.
        """
        # out of the range
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l, h = 0, m*n - 1
        while(l <= h):
            mid = l + (h-l)//2

            i = mid // n
            j = mid % n
            val = matrix[i][j]
            if val == target:
                return True
            
            # if it's less than the target (it's in the second half)
            if val < target:
                l = mid + 1
            # if it's more than the target (it's in the first half)
            else:
                h = mid - 1
        
        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))