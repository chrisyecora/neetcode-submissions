# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, boundary) -> bool:
            if not node:
                return True

            if node.val <= boundary[0] or node.val >= boundary[1]:
                return False
            
            return dfs(node.left, (boundary[0], node.val)) and dfs(node.right, (node.val, boundary[1]))
            
        return dfs(root.left, (float('-inf'), root.val)) and dfs(root.right, (root.val, float('inf')))
