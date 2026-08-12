# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isReallyValidBST(root, float('-inf'), float('inf'))

    def isReallyValidBST(self, root, val1, val2):
        if not root:
            return True
        c1, c2 = True, True
        if root.left:
            c1 = root.val > root.left.val > val1 and self.isReallyValidBST(root.left, val1, root.val)
        if root.right:
            c2 = root.val < root.right.val < val2 and self.isReallyValidBST(root.right, root.val, val2)
        return c1 and c2