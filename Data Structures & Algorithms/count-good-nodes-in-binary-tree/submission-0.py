# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isGood(self, root, val):
        return root.val >= val

    def goodNodes(self, root: TreeNode) -> int:
        return self.isGoodNodes(root, float('-inf'))
    
    def isGoodNodes(self, root, val):
        count = 0
        if root:
            count += 1 if self.isGood(root, val) else 0
            count += self.isGoodNodes(root.left, max(val, root.val)) + self.isGoodNodes(root.right, max(val, root.val))
        return count