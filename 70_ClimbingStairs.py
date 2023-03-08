import math

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        2 -> 1 + 1 / 2
        3 -> 1 + 1 + 1 / 1 + 2 / 2 + 1
        4 -> 1 + 1 + 1 + 1 / 1 + 2 + 1 / 1 + 1 + 2 / 2 + 1 + 1 / 2 + 2
        """
        # at most n additions
        # it depends on how many 2s you're using
        # for each number of additions, determine how many 2s can be used
        count = 0
        for i in range(n, 0 , -1):
            # if it can't add up to n even when using all 2s
            if i*2 < n:
                continue
            number_of_twos = n - i
            # then calculate the combinations of 2s positions possible
            count += math.comb(i, number_of_twos)
        
        return count

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))