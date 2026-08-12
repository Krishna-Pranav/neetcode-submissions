# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inord(root, result, 0)
        return result
    def inord(self, root, result, h):
        if root:
            if len(result) == h:
                result.append(root.val)
            self.inord(root.right, result, h+1)
            self.inord(root.left, result, h+1)
