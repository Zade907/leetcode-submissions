# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast,prev_slow = head,head,None
        while fast and fast.next != None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        if head.next is None:
            return None
        
        prev_slow.next = slow.next
        return head
