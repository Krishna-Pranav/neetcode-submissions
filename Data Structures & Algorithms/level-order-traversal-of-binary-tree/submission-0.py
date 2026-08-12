# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root:
            return []
        q.append((root, 0))
        result = []
        while q:
            temp, lvl = q.popleft()
            if len(result) > lvl:
                result[lvl].append(temp.val)
            else:
                result.append([temp.val])
            if temp.left:
                q.append((temp.left, lvl+1))
            if temp.right:
                q.append((temp.right, lvl+1))
        return result