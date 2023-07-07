# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def solve(root,target,sum,path,result):
            if not root:
                return
            sum+=root.val
            path.append(root.val)
            if sum==target and not root.left and not root.right:
                result.append(path.copy())
            solve(root.left,target,sum,path,result)
            solve(root.right,target,sum,path,result)

            sum-=root.val
            path.pop()

        result=[]
        path=[]
        solve(root,targetSum,0,path,result)
        return result
