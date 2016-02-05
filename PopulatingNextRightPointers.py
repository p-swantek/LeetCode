'''
Problem statement:
Given a binary tree(containing a TreeNode left, right, and next pointer) populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Note:
You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

Test cases passed: 14/14
Runtime: 108 ms
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        
        #base case, if the left subtree isn't null
        if root.left:
			
			#set that subtree's next pointer to point to the right subtree
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)