'''
Problem statement:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Test cases passed: 192/192
Runtime: 52 ms
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        return isSymmetricRecursive(root.left, root.right) #recursively check if each subtree is symmetric
        

def isSymmetricRecursive(left, right):
    if left is None and right is None: #base case, if both subtrees are None, this is a symmetric tree
        return True
    elif left is None or right is None: #base case, if either of the subtrees are None, then this tree isn't symmetric
        return False
    elif left.val != right.val: #base case, if the values of the left subtree and right subtree aren't equal, tree isn't symmetric
        return False
        
	#recursively check if the subtrees are symmetric
    return isSymmetricRecursive(left.left, right.right) and isSymmetricRecursive(left.right, right.left)