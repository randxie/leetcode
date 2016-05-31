class Solution(object):
    def isPalindrome(self, x):
        tmp = str(x)
        return tmp==tmp[::-1