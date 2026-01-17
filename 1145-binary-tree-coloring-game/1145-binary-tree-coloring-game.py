# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        dic = defaultdict(int)
        cur = TreeNode(0)

        def dfs(node):
            nonlocal cur
            if not node:
                return 0

            if node.val == x:
                cur = node
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            dic[node.val] = l + r
            return 1 + dic[node.val]
        
        dfs(root)

        if dic[root.val] - dic[x] > n // 2:
                return True
        
        if cur.left and dic[cur.left.val] + 1 > n // 2:
            return True
        
        if cur.right and dic[cur.right.val] + 1 > n // 2:
            return True

        return False





        # {3:2, 6:1, 7:1, }

        # if num_nodes > n // 2
        # {1:4, 3:3, 2;2, 4:1, 5:0}