# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = deque()
        deq = deque([root])
        while deq:
            l = len(deq)
            temp = []
            for _ in range(l):
                cur = deq.popleft()
                temp.append(cur.val)
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
            res.appendleft(temp)
        return list(res)