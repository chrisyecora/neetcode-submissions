# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # found the node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_val = self.findMinVal(root.right)
                root.right = self.deleteNode(root.right, min_val)
                root.val = min_val
        
        return root




    def findMinVal(self, curr: TreeNode) -> int:
        while curr and curr.left:
            curr = curr.left
        
        return curr.val