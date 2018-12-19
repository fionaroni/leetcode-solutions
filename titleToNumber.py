#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:47:13 2018

@author: fiona
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        row = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, \
               "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, \
               "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, \
               "V":22, "W":23, "X":24, "Y":25, "Z":26}
        if len(s) == 1:
            return row[s]
        else:
            first_letter = s[0]
            second_letter = s[1]
            print(first_letter)
            return row[first_letter]*26+row[second_letter]

myInstance = Solution()
answer = myInstance.titleToNumber("ZY")
print("singleNumber answer:", answer)
