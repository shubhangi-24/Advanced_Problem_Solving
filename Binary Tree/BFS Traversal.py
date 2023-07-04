def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        if root:
            queue.append(root)
        ans=[]
        while queue:
            level=[]
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)
        return ans
