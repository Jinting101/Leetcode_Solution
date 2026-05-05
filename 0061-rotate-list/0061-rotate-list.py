# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        j = n - k % n
        if j == 0 or j == n:
            return head
        prev, cur = None, head
        for _ in range(j):
            prev = cur
            cur = cur.next
        new_head = cur
        print(cur.val)
        while cur.next:
            cur = cur.next
        cur.next = head
        prev.next = None
        return new_head

            