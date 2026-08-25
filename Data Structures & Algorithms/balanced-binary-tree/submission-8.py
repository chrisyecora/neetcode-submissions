# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def dfs(node):
            if not node:
                return 0

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            if abs(right - left) > 1:
                self.valid = False
            return 1 + max(dfs(node.left), dfs(node.right))

        if not root:
            return True

        dfs(root)
        return self.valid

