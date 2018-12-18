#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:03:51 2018

@author: fiona
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # get numbers list
        nums = list(range(n+1))[1:]
        result = []
        for i in nums:
            if i % 5 == 0 and i % 3 == 0:
                result.append('FizzBuzz')
            elif i % 5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))
        return result
    
# create instance
myInstance = Solution()
answer = myInstance.fizzBuzz(15)
print("fizzBuzz answer:", answer)