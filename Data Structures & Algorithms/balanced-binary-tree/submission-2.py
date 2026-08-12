# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = True
        def dfs(node):
            if not node:
                return 0
            nonlocal check
            l = dfs(node.left)
            r = dfs(node.right)
            if abs(l-r) > 1:
                check = False
            return max(l, r)+1
        dfs(root)
        return check