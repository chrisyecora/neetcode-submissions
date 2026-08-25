# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()

                # solution
                if i == 0:
                    res.append(curr.val)

                if curr.right:
                    queue.append(curr.right)
                
                if curr.left:
                    queue.append(curr.left)

        return res

                
