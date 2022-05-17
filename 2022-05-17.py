# Problem 2022-05-17
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# Language: Python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.targ = None
        self.findTarget(original, cloned, target)
        return self.targ
    
    def findTarget(self, original, cloned, target):
        if original == target:
            self.targ = cloned
        
        if not original.left is None:
            self.findTarget(original.left, cloned.left, target)
        
        if not original.right is None:
            self.findTarget(original.right, cloned.right, target)
