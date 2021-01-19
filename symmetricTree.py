# -*- coding: utf-8 -*-
"""
Project: python-cookbook
Create Time: 2021/1/19 20:21
Author: Li Luyao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 判断一个二叉树是否对称，实质上是判断他的左子树和右子树是否对称
# 而左子树和右子树对称的条件是：左子树的左子树和右子树的右子树对称 and 左子树的右子树和右子树的左子树对称【递归】
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        def isTreeSymmetric(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                return isTreeSymmetric(left.left, right.right) and isTreeSymmetric(left.right, right.left)

        return True if isTreeSymmetric(root.left, root.right) else False

