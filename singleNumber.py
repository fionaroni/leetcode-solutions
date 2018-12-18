#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:04:21 2018

@author: fiona
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for g in nums: 
            count = nums.count(g)
            if count == 1:
                return g
    
myInstance = Solution()
answer = myInstance.singleNumber([1,0,1])
print("singleNumber answer:", answer)
