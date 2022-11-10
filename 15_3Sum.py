import numpy as np

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()

        neg, pos, zero = [], [], []

        # classify by positive, negative, and zeros 
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zero.append(num)
        
        # create a separate set for O(1) lookups
        N, P = set(neg), set(pos)

        # if there exists a zero, check for possibility where there is a matching positive and negative number
        if zero:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
        
        # if more than 3 zeros, add a triple of zeros
        if len(zero) >= 3:
            res.add((0, 0, 0))

        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                # check if the negative numbers add up to a positive number
                target = -(neg[i] + neg[j])
                if target in P:
                    res.add(tuple(sorted([neg[i], neg[j], target])))
        
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                # check if the positive numbers add up to a negative number
                target = -(pos[i] + pos[j])
                if target in N:
                    res.add(tuple(sorted([pos[i], pos[j], target])))
        
        return res

        # if len(nums) <= 3:
        #     if sum(nums) == 0:
        #         return [nums]
        #     else:
        #         return []
        # else:
        #     result = []
        #     for i in range(len(nums)):
        #         temp = nums[i+1:]
        #         while len(temp) > 1:
        #             popped = temp.pop()
        #             twoSum = nums[i] + popped
        #             if -twoSum in temp:
        #                 threeSum = [nums[i], popped, -twoSum]
        #                 threeSum.sort()
        #                 if threeSum not in result:
        #                     result.append(threeSum)
        #     return result
            

nums1 = [-1, 0, 1, 2, -1, -4] # output: [[-1,-1,2],[-1,0,1]]
nums2 = [0, 1, 1] # output: []
nums3 = [0, 0, 0] # output: [[0,0,0]]

print(Solution().threeSum(nums1))