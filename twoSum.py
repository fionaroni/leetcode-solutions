#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:42:53 2018

@author: fiona
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        diff_dict = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            diff_dict[diff] = i # map difference to index
            if diff in nums:
                answer.append(i)
        return answer

# create instance
myInstance = Solution()
answer = myInstance.twoSum([2,7,11,15], 9)
print("twoSum answer:", answer)