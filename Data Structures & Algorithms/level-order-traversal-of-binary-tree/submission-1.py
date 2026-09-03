# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ans = []
        # q = deque()
        # q.append(root)
        # while q:
        #     node = q.popleft()
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        # return ans
        if not root:
            return []

        ans = []
        q = deque()
        q.append(root)
        while q:
            level = []
            numNodes = len(q)
            for i in range(numNodes):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans