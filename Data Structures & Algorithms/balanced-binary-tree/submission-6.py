# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        
        left_tree = self.DFS(root.left)
        right_tree = self.DFS(root.right)

        if abs(left_tree - right_tree) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def DFS(self, root) -> int:
        if not root:
            return 0
               
        return 1 + max(self.DFS(root.left), self.DFS(root.right))