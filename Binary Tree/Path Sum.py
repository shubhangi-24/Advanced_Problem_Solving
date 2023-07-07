# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root,target,s):
            if not root:
                return 
            s+=root.val
            if not root.left and not root.right:
                if s==target:
                    return True
                else:
                    return False
            return solve(root.left,target,s) or solve(root.right,target,s)
        return solve(root,targetSum,0)
