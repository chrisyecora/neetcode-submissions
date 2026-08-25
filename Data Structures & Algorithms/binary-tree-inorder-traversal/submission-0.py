# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, arr): 
            if not node:
                return None
            
            if node.left:
                traverse(node.left, arr)

            arr.append(node.val)

            if node.right:
                traverse(node.right, arr)
    
        ans = []
        traverse(root, ans)
        return ans

        


        