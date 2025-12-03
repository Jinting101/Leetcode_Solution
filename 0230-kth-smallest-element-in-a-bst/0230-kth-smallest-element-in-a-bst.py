# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = [0]
        res = [0]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            cnt[0] += 1
            if cnt[0] == k:
                res[0] = node.val
                return
            inorder(node.right)
        inorder(root)
        return res[0]