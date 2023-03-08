class Solution(object):
    def generateParenthesis(self, n):
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        :type n: int
        :rtype: List[str]
        """
        # if n = 2: "(())", "()()"
        # if n = 3: "((()))", "()()()", "(()())", "(())()", "()(())"
        # if n = 4: "(((())))", "()()()()", "(()()())", "((()))()", "()((()))", "(())(())", "(()())()", "()(()())"
        # it depends on how many the outermost parenthesis can contain..

        paren = ""
        answer = []

        def solve(paren, n):
            leftParen, rightParen = countParenthesis(paren)
            print('left:', leftParen, '/ right:', rightParen)

            # all parenthesis have been found
            if leftParen == n and rightParen == n:
                answer.append(paren)
            
            # add a left parenthesis if it's under n
            if leftParen < n:
                print("added '(', now: '" + paren + "('")
                solve(paren + "(", n)
            # add a right parenthesis if it's under n AND i have matching number of left parenthesis
            if rightParen < n and rightParen < leftParen:
                print("added ')', now: '" + paren + ")'")
                solve(paren + ")", n)

        def countParenthesis(paren):
            return paren.count("("), paren.count(")")
        
        solve(paren, n)
        return answer

print(Solution().generateParenthesis(8))