# -*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
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
