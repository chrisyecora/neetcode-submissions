"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node, arr):
            if not node:
                return None
            
            for child in node.children:
                dfs(child, res)
            res.append(node.val)

        res = []
        dfs(root, res)
        return res

        

            
        