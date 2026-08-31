# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        left_boundary = float("-inf")
        right_boundary = float("inf")

        def validBinSubtree(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
                      

            return validBinSubtree(node.left, left, node.val) and validBinSubtree(node.right, node.val, right)

        return validBinSubtree(root, left_boundary, right_boundary)