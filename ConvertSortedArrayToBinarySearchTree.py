'''
Problem statement:
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Test cases passed: 32/32
Runtime: 112 ms
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
		#base case, if array length is 1 or less, just return a TreeNode from the single element in the array
        if len(nums) <= 1:
            return TreeNode(nums[0])
        
        mid = len(nums)//2 #get the midpoint
        
        root = TreeNode(nums[mid]) #make new TreeNode fromt the midpoint element
		
		#recursively set the left and right subtrees of the root TreeNode with the left half and right half of the array respectively
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root