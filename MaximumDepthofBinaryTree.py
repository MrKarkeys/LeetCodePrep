# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            popped = stack.pop()
            if popped[0]:
                res = max(res, popped[1])
                stack.append([popped[0].left, popped[1]+1])
                stack.append([popped[0].right, popped[1]+1])
        return res
                
