# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def find(p,q):
            if(p==None and q==None):
                return True
            elif((p==None and q!= None) or (p!=None and q==None) or (q.val!=p.val)):
                return False
            return find(p.left,q.left) and find(p.right,q.right)
        return find(p,q)