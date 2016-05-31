import math
class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        else:
            b = math.log(n)/math.log(3)
            b = round(b)
            return ((3**b == n) or (3**(b-1) == n) or (3**(b+1) == n))
        
        """
        :type n: int
        :rtype: bool
        """
