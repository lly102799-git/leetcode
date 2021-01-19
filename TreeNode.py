# -*- coding: utf-8 -*-
"""
@project: python-cookbook
@date: 2021-01-19 16:34
@author: Li Luyao
"""
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


treenode_a = TreeNode('A')
treenode_b = TreeNode('B')
treenode_c = TreeNode('C')
treenode_d = TreeNode('D')
treenode_e = TreeNode('E')
treenode_f = TreeNode('F')

treenode_a.left = treenode_b
treenode_a.right = treenode_c
treenode_b.left = treenode_d
treenode_b.right = treenode_e
treenode_c.right = treenode_f


def preorder(root):
    if not root:
        return
    print(root.val)

    preorder(root.left)
    preorder(root.right)

preorder(treenode_a)

