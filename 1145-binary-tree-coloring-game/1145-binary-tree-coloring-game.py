# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        
        dic = defaultdict(int)
        lr = [0, 0]

        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            if node.val == x:
                lr[0] = l
                lr[1] = r
            
            tot = l + r
            return 1 + tot
        
        total = dfs(root)
        maxp = max(lr)

        if n - (1 + lr[0] + lr[1]) > n //2:
            return True
        
        if maxp > n // 2:
            return True

        return False





        # {3:2, 6:1, 7:1, }

        # if num_nodes > n // 2
        # {1:4, 3:3, 2;2, 4:1, 5:0}