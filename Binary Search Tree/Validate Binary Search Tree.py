class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root,lower,upper):
            if root==None:
                return True
            if root.val>lower and root.val<upper:
                return solve(root.left,lower, root.val) and solve(root.right,root.val,upper)
            return False

        return solve(root,-inf,inf)    
