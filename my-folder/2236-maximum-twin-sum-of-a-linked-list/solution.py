# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev_slow, slow, fast = None, head,head
        sum = 0
        if not head.next.next:
            return head.val + head.next.val
        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev_slow
            prev_slow = slow
            slow = temp
        while slow and prev_slow:
            if slow.val + prev_slow.val > sum:
                sum = slow.val + prev_slow.val 
            slow = slow.next
            prev_slow = prev_slow.next
        return sum
