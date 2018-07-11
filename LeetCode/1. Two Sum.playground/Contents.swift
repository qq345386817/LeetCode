//: Playground - noun: a place where people can play

import UIKit

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int: Int]()
        
        for (idx, num) in nums.enumerated() {
            let minus = target - num
            if dict[minus] != nil {
                return [dict[minus]!, idx]
            }
            dict[num] = idx
        }
        return [Int]()
    }
}

let obj = Solution()
let nums = [3, 2, -4]
let target = -1

print(obj.twoSum(nums, target))
print(obj.twoSum([0, 4, -2, 88], 88))
