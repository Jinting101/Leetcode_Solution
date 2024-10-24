# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def checker(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return ((checker(node1.left, node2.left) or checker(node1.left, node2.right)) and
                    (checker(node1.right, node2.right) or checker(node1.right, node2.left)))
        
        return checker(root1, root2)


# Base Cases:
    # If both root1 and root2 are None, they are flip equivalent, so return True.
    # If one is None and the other is not, return False.
    # If the values at root1 and root2 are different, return False.


# Recursive Cases:
# The function recursively checks two scenarios:
    # No flip: The left subtree of root1 is compared with the left subtree of root2, and the right subtree of root1 is compared with the right subtree of root2.
    # Flip: The left subtree of root1 is compared with the right subtree of root2, and the right subtree of root1 is compared with the left subtree of root2.
    
# If either scenario returns True, the trees are flip equivalent.