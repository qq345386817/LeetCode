# -*- coding: utf-8 -*-

class ListNode:
    '''
    val: Node 保存的数据
    next: 指向下一个节点
    '''
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def append(self, node):
        self.next = node
        return self

    def __repr__(self):
        '''
        定义 Node 的 print 输出
        '''
        result = str(self.val)
        nextNode = self.next
        while nextNode != None:
            result = result + " -> " + str(nextNode.val)
            nextNode = nextNode.next
        return result

class Solution:
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        p = l1
        q = l2
        while p != None or q != None:
            x = 0
            y = 0
            if p != None:
                x = p.val
                p = p.next
            if q != None:
                y = q.val
                q = q.next
            sum = x + y + carry
            carry = sum // 10  # 整除
            newNode = ListNode(sum % 10)
            curr.next = newNode
            curr = newNode
        if carry > 0 :
            curr.next = ListNode(1)
        return dummy.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        sum = l1.val + l2.val
        result = ListNode(sum % 10)
        nextNode1 = l1.next
        if sum >= 10:
            nextNode1 = self.addTwoNumbers(nextNode1, ListNode(1))
        result.next = self.addTwoNumbers(nextNode1, l2.next)

        return result
        
node1 = ListNode(2).append(ListNode(4).append(ListNode(3)))
node2 = ListNode(5).append(ListNode(6).append(ListNode(4)))

print(node1)
print(node2)
so = Solution()
# print(so.addTwoNumbers2(node1,node2))
print(so.addTwoNumbers2(ListNode(1).append(ListNode(8)),ListNode(0)))
print(so.addTwoNumbers2(ListNode(5),ListNode(5)))
