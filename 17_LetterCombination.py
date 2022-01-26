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
        for i in digits:
            print(Solution.letterMapping[i])


def main():
    Solution.letterCombinations("??", "23")

if __name__ == "__main__":
    main()