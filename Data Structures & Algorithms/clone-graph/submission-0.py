"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloner(self, node, nodeMap):
        if node.val not in nodeMap:
            temp = Node(node.val)
            nodeMap[node.val] = temp
        for n in node.neighbors:
            if n.val in nodeMap:
                nodeMap[node.val].neighbors.append(nodeMap[n.val])
            else:
                nodeMap[node.val].neighbors.append(self.cloner(n, nodeMap))
        return nodeMap[node.val]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        nodeMap = {}
        cloneNode = self.cloner(node, nodeMap)
        return cloneNode