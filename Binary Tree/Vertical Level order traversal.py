# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solve(root, col, row, map):
            if not root:
                return 
            if col not in map:
                map[col] = []
            map[col].append((row, root.val))
            solve(root.left, col-1, row+1, map)
            solve(root.right, col+1, row+1, map)
        
        map = OrderedDict()
        result = []
        solve(root, 0, 0,  map)
        for col in sorted(map.keys()):  
            column_values = [node[1] for node in sorted(map[col])]  
            result.append(column_values)
        
        return result
