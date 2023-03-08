class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        rightSum = sum(nums) # we start from the left
        for i in range(len(nums)):
            if i > 0:
                leftSum += nums[i-1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
        return -1

print(Solution().pivotIndex([2,1,-1]))