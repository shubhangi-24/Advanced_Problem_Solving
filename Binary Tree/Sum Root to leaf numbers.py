# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result=0
    
        def solve(root,val):
            if root==None:
                return 
            val=val*10+root.val
            if (root.left==None and root.right==None):
                self.result+=val
            solve(root.left,val)
            solve(root.right,val)

        solve(root,0)
        return self.result
