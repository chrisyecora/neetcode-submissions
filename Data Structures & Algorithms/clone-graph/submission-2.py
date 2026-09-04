"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        def clone(n):
            if not n:
                return None
            if n.val in clones:
                return clones[n.val]
            
            newNode = Node(n.val)
            clones[n.val] = newNode

            for neigh in n.neighbors:
                newNode.neighbors.append(clone(neigh))
            return newNode

        return clone(node)