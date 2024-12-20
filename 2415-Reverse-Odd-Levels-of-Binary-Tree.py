# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque()
        q.append(root)
        rev=False
        while q:
            qz=len(q)
            arr=[]
            for i in range(qz):
                Node=q.popleft()
                if Node.left: q.append(Node.left)
                if Node.right: q.append(Node.right)
                if rev:
                    arr.append(Node)
                    if i>=qz/2:
                        arr[i].val, arr[qz-1-i].val=arr[qz-1-i].val, arr[i].val
            rev=not rev
        return root

        
        l = 0
        q = deque([root])
        res = []
        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    if l % 2 == 0:
                        res.append(cur.left.val)
                if cur.right:
                    q.append(cur.right)
                    if l % 2 == 0:
                        res.append(cur.right.val)
                if l % 2 == 1:
                    cur.val = res.pop()
            l += 1
        return root