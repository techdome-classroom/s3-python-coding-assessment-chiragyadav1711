class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        matching_bracket = {')' : '(' , '}' : '{' , ']' : ' ['}

        stack = []

        for char in s

        if char in matching_bracket:
            top_element = stack.pop() if stack else '#'

        if matching_bracket[char] != top_element:
            return false

        else:
            stack.append(char)

        return not stack

        solution = Solution()

        print(solution.isValid("()"))
        print(solution.isValid("() [] {}"))
        print(solution.isValid("(]"))
        
       






    



  

