# Problem 2022-05-13
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Language: Python3

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        self.tree = dict()
        self.connectHelper(root, 0)
        
        return root
        
    def connectHelper(self, node, level):
        if not level in self.tree.keys():
            self.tree[level] = node
        else:
            node.next = self.tree[level]
            self.tree[level] = node
        
        if not node.right is None:
            self.connectHelper(node.right, level+1)
        
        if not node.left is None:
            self.connectHelper(node.left, level+1)
            
        return
