# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if root:
            return 1+max(self.height(root.left), self.height(root.right))
        return 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and (-1 <= self.height(root.left)-self.height(root.right) <= 1)