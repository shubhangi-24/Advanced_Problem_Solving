class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        while True:
            while root!=None:
                stack.append(root)
                root=root.left

            root=stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right
