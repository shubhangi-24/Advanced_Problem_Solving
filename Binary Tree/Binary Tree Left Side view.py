def LeftView(root):
    queue=deque()
    if root:
        queue.append(root)
    ans=[]
    while queue:
        n=len(queue)
        for i in range(n):
            node=queue.popleft()
            if i==0:
                ans.append(node.data)
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
        
