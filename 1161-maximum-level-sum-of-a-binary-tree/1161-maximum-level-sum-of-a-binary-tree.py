# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxl = 1
        maxs = -float('inf')
        q = deque([root])
        curl = 1
        while q:
            l = len(q)
            curs = 0
            for _ in range(l):
                cur = q.popleft()
                curs += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if curs > maxs:
                maxs = curs
                maxl = curl
            curl += 1
        return maxl
