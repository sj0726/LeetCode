class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = 0
        result = [0] * len(nums)
        for i in range(len(nums)):
            runningSum += nums[i]
            result[i] = runningSum

        return result

print(Solution().runningSum([3,1,2,10,1]))