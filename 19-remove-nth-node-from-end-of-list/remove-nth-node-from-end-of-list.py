# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node simplifies edge cases like removing the head node
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Advance fast pointer so that the gap between fast and slow is n + 1 nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both fast and slow until fast reaches the end (None)
        while fast:
            fast = fast.next
            slow = slow.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next