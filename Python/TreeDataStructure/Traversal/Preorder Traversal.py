"""
Given a binary tree, return the preorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,2,3].
"""


class Solution:

    def inorder_traversal(self, root):

        result, stack = [], [(root, False)]

        while stack:
            root, is_flaged = stack.pop()
            if root is None:
                continue
            if is_flaged:
                result.append(root.data)
            else:
                stack.append((root.right, False))
                stack.append((root.left, False))
                stack.append((root, True))

        return result
    # Using recursion
    def preorderTraversal(self, root):
        res  = []
        if root is None:
            return res
        self.helper(root, res)
        return res

    def helper(self, node, res):

        if node is None:
            return
        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)


""" Testing Code """
from Python.Level6.TreeDataStructure import Node

s = Solution()
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
print(s.inorder_traversal(root))
