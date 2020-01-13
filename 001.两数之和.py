'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

#答：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            # 主要逻辑都在内部函数中实现
            def add(a,b,carry):
                # 递归的终止条件是a和b都为空
                # 如果carry大于0需要返回一个进位标志
                if not (a or b):
                    return ListNode(1) if carry else None
                # 如果a为空则将ListNode(0)赋给a，对于b也是
                a = a if a else ListNode(0)
                b = b if b else ListNode(0)
                #处理val，以及进位标志
                val = a.val + b.val + carry
                carry = 1 if val>=10 else 0
                a.val = val%10
                # 现在a的值就是两个节点相加后的和了
                # 之后再次递归计算a.next和b.next
                a.next = add(a.next,b.next,carry)
                return a
            return add(l1,l2,0)
