# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Push the head of each non-empty linked list into the heap
        # Use list index `i` as a tie-breaker to avoid direct comparison between ListNode instances
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # If there is a next node in the same list, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next