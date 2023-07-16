 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
    def __init__(self,min_val,max_val,Sum):
        self.min_val=min_val
        self.max_val=max_val
        self.Sum=Sum

class Solution:
    
    def solve(self,root):
        if root==None:
            return Node(inf,-inf,0)

        left=self.solve(root.left)
        right=self.solve(root.right)

        if left==None or right==None:
            return None

        if root.val>left.max_val and root.val<right.min_val:
            currSum=left.Sum+right.Sum+root.val
            self.maxSum=max(self.maxSum,currSum)
            return Node(min(root.val,left.min_val),max(root.val,right.max_val),currSum)

        return None

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum=0
        ans=self.solve(root)
        return self.maxSum



        
