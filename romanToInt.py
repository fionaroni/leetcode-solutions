#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:02:46 2018

@author: fiona
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        
        # create dictionary with symbol-value mappings
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, \
             'IV':4, 'IX':9, 'XL':40, 'XC': 90, 'CD':400, 'CM':900}
        
        # split string into letters, exclude delimeters
#        letters = re.split('IV|IX|XL|XC|CD|CM', s)
        # split string into letters, include delimeters
        letters = re.split(r"(IV|IX|XL|XC|CD|CM)", s)
        no_empty_str = [l for l in letters if l != '']
        print(no_empty_str)
        
        # convert letters to corresponding integers
        nums = [d[k] for k in no_empty_str]
#        nums = list(map(d.get, no_empty_str))
        print(nums)
        
        # add values
        return sum(nums)

# create instance
myInstance = Solution()
answer = myInstance.romanToInt("XIV")
print("romanToInt answer:", answer)

def romanToInt2(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    # for loop executes once for each letter
    # except for last letter because it cannot compare itself to next value
    for i in range(len(s)-1): 
        print(i) # notice last for loop doesn't execute because there is no s[i+1] to compare
        if roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
            print("result is now", result)
        else:
            result += roman[s[i]]
    return result + roman[s[-1]] # add last letter

XIV = romanToInt2("XIV")
XVII = romanToInt2("XVII")
print("XIV equals:", XIV)
print("XVII equals:", XVII)