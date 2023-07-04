# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]

        q=deque()
        p_map={}
        if root:
            q.append(root)

        while q:
            node=q.popleft()
            if node.left:
                q.append(node.left)
                p_map[node.left]=node
            if node.right:
                q.append(node.right)
                p_map[node.right]=node
            
        q.append(target)
        dis=0
        visited=set()
        visited.add(target)

        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if node in p_map and p_map[node] not in visited:
                    q.append(p_map[node])
                    visited.add(p_map[node])
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
            dis+=1
            if dis==k:
                break
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node.val)
        return ans
        
