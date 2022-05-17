# Problem 2022-05-15
# https://leetcode.com/problems/deepest-leaves-sum/
# Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.deepest = -1
        self.deepestVal(root, 0)
        return self.sum
            
    def deepestVal(self, node, level):
        if not node.left is None:
            self.deepestVal(node.left, level+1)
        
        if not node.right is None:
            self.deepestVal(node.right, level+1)
        
        
        if level > self.deepest:
            self.sum = node.val
            self.deepest = level
        elif level == self.deepest:
            self.sum += node.val
            
        return
