# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:12:17 2016

@author: randxie
"""

# from https://www.hrwhisper.me/leetcode-verify-preorder-serialization-of-a-binary-tree/
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for x in preorder.split(','):
            stack += [x]
            while len(stack) >= 3 and stack[-2:] == ['#','#'] and stack[-3]!='#':
                stack = stack[:-3] +['#'] # pop *3 and append #
        return len(stack) == 1 and stack[0] == '#'