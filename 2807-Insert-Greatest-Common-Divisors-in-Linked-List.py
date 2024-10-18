# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if head.next is None:
            return head
        
        cur = head
        while cur.next:
            gcd = get_gcd(cur.val, cur.next.val)
            temp = ListNode(gcd, cur.next)
            cur.next = temp
            cur = cur.next.next
        return head