def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        ans=[]
        if root:
            q.append(root)
        while q:
            for i in range(len(q)):
                node=q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(node.val)

        return ans
