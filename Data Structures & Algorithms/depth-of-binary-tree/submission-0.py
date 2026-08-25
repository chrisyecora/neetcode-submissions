# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.dfs(1, root)


    def dfs(self, level, node):
        if not node:
            return level - 1
        
        return max(self.dfs(level + 1, node.left), self.dfs(level + 1, node.right))







