//
//  main.swift
//  2. AddTwoNumbers
//
//  Created by mac on 2018/7/9.
//  Copyright © 2018年 luopeike. All rights reserved.
//

import Foundation

/**
 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
 
 示例：
 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
 输出：7 -> 0 -> 8
 原因：342 + 465 = 807
 */

public class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int) {
        self.val = val
        next = nil
    }
    
    func setNext(_ nextLi: ListNode?) -> ListNode {
        self.next = nextLi
        return self
    }
    
    func description() -> String {
        var nextNode = self.next
        var result = "\(self.val)"
        while nextNode != nil {
            result += " -> \(nextNode!.val)"
            nextNode = nextNode?.next
        }
        return result
    }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        guard let l2 = l2 else { return l1 }
        guard let l1 = l1 else { return l2 }
        let sum = l1.val + l2.val
        let result = ListNode(sum % 10)
        var nextNode1 = l1.next
        if sum >= 10 {
            nextNode1 = addTwoNumbers(nextNode1, ListNode(1))
        }
        result.next = addTwoNumbers(nextNode1, l2.next)
        return result
    }
}

let l1 = ListNode(2).setNext(ListNode(4).setNext(ListNode(3)))
let l2 = ListNode(5).setNext(ListNode(6).setNext(ListNode(4)))

print(l1.description())
print(l2.description())
print(Solution().addTwoNumbers(l2, l1)?.description() ?? "Nil Value...")
