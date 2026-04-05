# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def traveller(root):
            if not root:
                return

            traveller(root.left)
            arr.append(root.val)
            traveller(root.right)
        
        traveller(root)
        return arr[k-1]