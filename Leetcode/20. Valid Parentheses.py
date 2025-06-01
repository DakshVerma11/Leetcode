class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        openbrackets=('(', '{', '[')
        closedbrackets=(')', '}', ']')
        bracketdict= {'(': ')', '{': '}', '[' : ']'}
        for i in s:
            if i in openbrackets:
                stack.append(i)
            elif i in closedbrackets:
                if not stack or bracketdict[stack[-1]]!=i:
                    return False
                stack.pop()
        if not stack:
            return True

        return False 
