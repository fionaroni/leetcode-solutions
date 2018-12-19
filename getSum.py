#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:07:18 2018

@author: fiona
"""

# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        l = [a, b]
        return sum(l)
    
myInstance = Solution()
answer = myInstance.getSum(-3,2)
print("singleNumber answer:", answer)
