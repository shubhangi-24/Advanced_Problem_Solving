# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(p,q):
            if p==None and q==None:
                return True
            if (p!=None and q==None) or (p==None and q!=None):
                return False
            if p.val!=q.val:
                return False
            return solve(p.left,q.right) and solve(p.right,q.left)
            

        return solve(root,root)
        
















        

            
