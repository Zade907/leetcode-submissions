# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prevSlow, slow,fast = None, head, head
        if not head.next.next:
            return head.val + head.next.val
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prevSlow
            prevSlow = slow
            slow = temp
        sum = 0 
        while slow and prevSlow:
            if slow.val + prevSlow.val > sum:
                sum = slow.val + prevSlow.val
            slow = slow.next
            prevSlow = prevSlow.next
        return sum
        
            

        

