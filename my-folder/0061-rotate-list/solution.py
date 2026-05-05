# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        n = 1
        tail = head
        while tail.next:
            tail = tail.next 
            n += 1
        k %= n
        tail.next = head
        newTail = head

        for _ in range(n - k - 1):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None

        return newHead
