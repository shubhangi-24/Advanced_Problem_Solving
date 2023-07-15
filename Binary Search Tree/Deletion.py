# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inordersuccessor(self,node):
            while node.left!=None:
                node=node.left
            return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)

        else:
            if root.left==None and root.right==None :
                return None
            elif root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                successorNode=self.inordersuccessor(root.right)
                root.val=successorNode.val
                root.right=self.deleteNode(root.right,successorNode.val)

        return root

    
