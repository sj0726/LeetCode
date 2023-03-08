class Solution(object):
    letterMapping = {
                        "2": ["a", "b", "c"],
                        "3": ["d", "e", "f"],
                        "4": ["g", "h", "i"],
                        "5": ["j", "k", "l"],
                        "6": ["m", "n", "o"],
                        "7": ["p", "q", "r", "s"],
                        "8": ["t", "u", "v"],
                        "9": ["w", "x", "y", "z"]
                    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        answers = Solution().letterMapping[digits[0]]
        if len(digits) == 1:
            return answers
        
        # if it's more than 1 long
        for i in digits[1:]:
            answers = [x + y for x in answers for y in Solution().letterMapping[i]]
        
        return answers
        

print(Solution().letterCombinations("3429"))