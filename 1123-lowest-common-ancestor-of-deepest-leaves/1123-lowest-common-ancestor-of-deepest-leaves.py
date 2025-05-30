# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if not node:
                # If node is None, return (None, current depth)
                return (None, depth-1)
            
            # Recursively traverse left and right children
            left_lca, left_depth = dfs(node.left, depth + 1)
            right_lca, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                # Left subtree is deeper → propagate its LCA and depth upward
                return (left_lca, left_depth)
            elif right_depth > left_depth:
                # Right subtree is deeper → propagate its LCA and depth upward
                return (right_lca, right_depth)
            else:
                # Both subtrees are at the same depth → current node is LCA
                return (node, left_depth)

        # Start recursive DFS from the root at depth 0
        lca_node, _ = dfs(root, 0)
        return lca_node