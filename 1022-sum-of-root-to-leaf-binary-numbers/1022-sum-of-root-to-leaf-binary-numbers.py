# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(root, '')])
        while q:
            l = len(q)
            for _ in range(l):
                node, path = q.popleft()
                path += str(node.val)
                if (not node.left) and (not node.right):
                    res += int(path, 2)
                if node.left:
                    q.append((node.left, path))
                if node.right:
                    q.append((node.right, path))
        return res