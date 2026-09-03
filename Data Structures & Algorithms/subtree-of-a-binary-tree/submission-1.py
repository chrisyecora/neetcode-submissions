# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subNode):
            if type(node) != type(subNode):
                return False
            if not node and not subNode:
                return True
            if node.val != subNode.val:
                return False
            else:
                return dfs(node.left, subNode.left) and dfs(node.right, subNode.right) 


        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                if node.val == subRoot.val:
                    if dfs(node, subRoot):
                        return True
                q.append(node.left)
                q.append(node.right)

        return False


            
