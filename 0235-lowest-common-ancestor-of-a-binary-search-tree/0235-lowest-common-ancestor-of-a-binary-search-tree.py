# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            leftreturn = lca(node.left, p, q)
            rightreturn = lca(node.right, p, q)
            if leftreturn and rightreturn:
                return node
            return leftreturn if leftreturn else rightreturn
        
        return lca(root, p.val, q.val)