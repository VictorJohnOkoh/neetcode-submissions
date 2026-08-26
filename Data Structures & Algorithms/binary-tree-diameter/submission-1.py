# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.treeDiameter(root)

    def treeDiameter(self, root) -> int:
        if not root:
            return 0
        curr = self.treeDepth(root.left) + self.treeDepth(root.right)
        return max(curr, self.treeDiameter(root.left), self.treeDiameter(root.right))
        
        

    def treeDepth(self, root) -> int:
        if not root:
            return 0

        return 1 + max(self.treeDepth(root.left), self.treeDepth(root.right))
        