# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def find(node):
            if (node == None):
                return
            find(node.left)
            ans.append(node.val)
            find(node.right)
        find(root)
        return (ans)