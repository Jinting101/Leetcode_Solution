# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        deq = deque([(root, -float('inf'))])
        while deq:
            l = len(deq)
            for _ in range(l):
                cur, curmax = deq.popleft()
                if cur.val >= curmax:
                    res += 1
                curmax = max(cur.val, curmax)
                if cur.left:
                    deq.append((cur.left, curmax))
                if cur.right:
                    deq.append((cur.right, curmax))
        return res