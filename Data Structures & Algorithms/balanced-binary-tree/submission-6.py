# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def height(node):
            if not node:
                return 0

            left = 1 + height(node.left)
            right = 1 + height(node.right)
            if abs(right - left) > 1:
                self.valid = False
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True

        height(root)
        return self.valid

