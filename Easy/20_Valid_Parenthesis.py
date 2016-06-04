class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            else:
                if(len(stack)==0):
                    return False
                tmp = stack.pop(-1)
                paired = False
                if(i==')' and tmp=='('):
                    paired = True
                if(i=='}' and tmp=='{'):
                    paired = True
                if(i==']' and tmp=='['):
                    paired = True
                if(not paired):
                    return False
        if len(stack)==0:
            return True
        else:
            return False
                
            
        """
        :type s: str
        :rtype: bool
        """