from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        middle = head
        tail = head
        while tail is not None and tail.next is not None:
            middle = middle.next
            tail = tail.next.next
        return middle
        