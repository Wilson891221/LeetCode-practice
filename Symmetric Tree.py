# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def find(r,l):
            if(r == None and l==None):
                return True
            if(r!=None and l!=None and r.val==l.val):
                return find(r.right,l.left) and find(r.left,l.right)
        return find(root.right,root.left)
        