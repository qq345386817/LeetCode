//: Playground - noun: a place where people can play

import UIKit

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if x < 0 || ((x % 10 == 0) && (x != 0)) {
            return false
        }
        var originalNum = x
        var reverseNum = 0
        while originalNum > reverseNum {
            reverseNum = reverseNum * 10 + originalNum % 10
            originalNum /= 10
        }
        return originalNum == reverseNum || originalNum == reverseNum/10
    }
}

let obj = Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(1234))
print(obj.isPalindrome(123321))
print(obj.isPalindrome(12321))
