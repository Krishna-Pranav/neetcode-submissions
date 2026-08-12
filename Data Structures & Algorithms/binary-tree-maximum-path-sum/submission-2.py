# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        self.maxiPa(root)
        return self.maxi
    def maxiPa(self, root):
        if root == None:
            return 0
        maxL = max(0, self.maxiPa(root.left))
        maxR = max(0, self.maxiPa(root.right))
        self.maxi = max(self.maxi, root.val+maxL+maxR)
        return root.val+max(maxL, maxR)
