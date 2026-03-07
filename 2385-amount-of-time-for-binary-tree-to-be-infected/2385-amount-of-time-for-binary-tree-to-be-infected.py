# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        lst = [0, 0]
        start_level = -1
        q = deque([(root, 0, 0)])
        while q:
            l = len(q)
            for _ in range(l):
                cur, level, d = q.popleft()
                if cur.val == start:
                    start_level = level
                lst[0] = max(lst[0], level)
                lst[1] = min(lst[1], level)

                if cur.left:
                    if cur.val == root.val:
                        d = 1
                    q.append((cur.left, level+d, d))
                if cur.right:
                    if cur.val == root.val:
                        d = -1
                    q.append((cur.right, level+d, d))

        return max(lst[0] - start_level, start_level - lst[1])

