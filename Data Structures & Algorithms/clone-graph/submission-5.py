"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}
        clones[node] = Node(node.val)
        q = deque([node])

        while q:
            n = q.popleft()
            for neigh in n.neighbors:
                if neigh not in clones:
                    clones[neigh] = Node(neigh.val)
                    q.append(neigh)
                clones[n].neighbors.append(clones[neigh])
        return clones[node]