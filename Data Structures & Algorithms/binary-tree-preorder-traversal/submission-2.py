# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, res):
            if not node:
                return

            res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)
        
        res = []
        dfs(root, res)
        return res

            