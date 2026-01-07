# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        total_sum = 0
        q = deque([root])
        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                total_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        res = [0]
        def calculate(cur, tot):
            res[0] = max(res[0], cur * (tot - cur))
        def inorder(node):
            if not node:
                return 0
            ls = inorder(node.left)
            rs = inorder(node.right)
            calculate(ls, total_sum)
            calculate(rs, total_sum)
            # calculate(node.val + ls + rs, total_sum)
            # print(node.val, ls, rs)
            return node.val + ls + rs
        inorder(root)
        return res[0] % MOD
