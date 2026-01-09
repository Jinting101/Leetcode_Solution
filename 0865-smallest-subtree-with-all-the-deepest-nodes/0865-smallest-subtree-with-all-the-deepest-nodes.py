# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = deque([root])
        deepest_node = []
        while d:
            deepest_node = d.copy()
            l = len(d)
            for _ in range(l):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)

        def lca(node, node1, node2):
            if not node or not node1 or not node2 or node.val == node1.val or node.val == node2.val:
                return node
            
            left = lca(node.left, node1, node2)
            right = lca(node.right, node1, node2)

            if left and right:
                return node
            
            return left if left else right

        while len(deepest_node) > 1:
            lca_node = lca(root, deepest_node[-1], deepest_node[-2])
            deepest_node.pop()
            deepest_node.pop()
            deepest_node.append(lca_node)
        
        return deepest_node[0]
