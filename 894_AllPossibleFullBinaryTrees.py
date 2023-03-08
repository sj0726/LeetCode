# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        1 <= n <= 20
        """
        dp = { # key: n / value: all possible FBTs with n nodes
            0: [],
            1: [TreeNode()]
        }

        # returns the list of all possible FBT with n nodes
        def backtrack(n):
            # check the cache
            if n in dp:
                return dp[n]
            
            result = []
            for l in range(n): # 0 through n-1 (excluding the root node)
                # right n - l (-1 added because we exlcude the root node)
                r = n - 1 - l
                # in the left
                leftTrees, rightTrees = backtrack(l), backtrack(r)

                # create all possible combinations of FBTs generated from leftTrees and rightTrees
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        # create a new full binary tree with n nodes
                        result.append(TreeNode(0, t1, t2))
            # store the result in the cache for faster computation in future cases
            dp[n] = result
            return result
        
        return backtrack(n)
