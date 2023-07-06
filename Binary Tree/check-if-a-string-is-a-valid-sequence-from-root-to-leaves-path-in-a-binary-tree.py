class Solution:
    def isValidSequence(self, root, arr):
        def solve(root, arr, i):
            if not root:
                return False
            if i>= len(arr):
                return False
            if root.val == arr[i]:
                if (i == len(arr)-1 and not root.left and not root.right) :
                    return True
                else:
                    return False
            return solve(root.left, arr, i+1) or solve(root.right, arr, i+1)
        
        return solve(root, arr, 0)
