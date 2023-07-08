from collections import OrderedDict
class Solution:
    def verticalTraversal(self, root):
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
            column_values = [node[1] for node in map[col]]  
            result.append(column_values)
        
        return result
