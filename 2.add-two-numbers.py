'''
Leetcode 2. add-two-numbers 
Easy

Amazon #2

while문을 만들때는 종료 기준을 먼저 쓰고 coding하기
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def display(self):
        curr = l1
        while curr:
            print("["+str(curr.val)+"]")
            curr = curr.next
        

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        
        head = l1
        while l1 is not None and l2 is not None:
            l1.val += l2.val

            if l1.val >= 10:
                l1.val = l1.val - 10
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
            
            if l1.next is None:
                last = l1

            l1 = l1.next
            l2 = l2.next
        
        if l2:
            last.next = l2
        else:
            while l1 is not None:
                if l1.val >= 10:
                    l1.val = l1.val - 10
                    if l1.next:
                        l1.next.val += 1
                    else:
                        l1.next = ListNode(1)
                l1 = l1.next
        
        return head
            
            
sol = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(6)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)


sol.addTwoNumbers(l1, l2).display()
        
            
