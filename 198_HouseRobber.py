class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1] * (len(nums) + 1)
        def solve(current):
            if current < 0:
                return 0
            if memo[current] >= 0:
                return memo[current]
            
            # 2 options: rob the current house, don't rob the current house
            memo[current] = max(solve(current-2) + nums[current], solve(current-1))
            return memo[current]
        
        return solve(len(nums)-1)
    
print(Solution().rob([1,2,3,1]))