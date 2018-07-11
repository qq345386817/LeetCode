# -*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        result = 0
        tempResult = 0
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= 0:
                if tempResult > result:
                    result = tempResult
                tempResult = 1
                i = dict[s[i]] + 1   # Error: Python 的 循环 不能回退
                dict = {}
            else:
                tempResult += 1
                dict[s[i]] = i
        if tempResult > result:
            result = tempResult
        return result

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subStr = ""
        result = 0
        for i in range(len(s)):
            subI = subStr.find(s[i])
            if subI > -1:
                subStr = subStr[(subI+1):] + s[i]
            else:
                subStr += s[i]
            if result < len(subStr):
                result = len(subStr)
        return result

so = Solution()
print(so.lengthOfLongestSubstring('abcabcbb'))
print(so.lengthOfLongestSubstring('bbbbb'))
print(so.lengthOfLongestSubstring('pwwkew'))
print(so.lengthOfLongestSubstring(''))
print(so.lengthOfLongestSubstring('dvdf'))

# 预期输出
'''
3
1
3
0
3
'''
