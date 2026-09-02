"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone(node, created):
            # base case
            if not node:
                return

            # prevent loops
            if node.val in created:
                return created[node.val]
            
            print(node.val)
            newNode = Node(node.val)
            created[newNode.val] = newNode
            for neighbor in node.neighbors:
                print("neigh", neighbor.val)
                newNode.neighbors.append(clone(neighbor, created))

            return newNode
                

        created = {}
        return clone(node, created)