# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None 
        prevSlow,slow, fast = None, head, head
        while fast and fast.next:
            prevSlow = slow
            fast = fast.next.next
            slow = slow.next
        prevSlow.next = slow.next
        return head

