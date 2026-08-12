# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        st = deque()
        st.append(root)
        temp = root.left
        while st or temp:
            while temp:
                st.append(temp)
                temp = temp.left
            temp = st.pop()
            result.append(temp.val)
            temp = temp.right
        return result[k-1]
