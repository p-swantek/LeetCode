'''
Problem statement:
Given a linked list, determine if it has a cycle in it.

Test cases passed: 16/16
Runtime: 80 ms
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        slowPointer = fastPointer = head #keep 2 pointers to the head of the list, a 'slow' and a 'fast' pointer
        
		#loop through the list based on the 'fast' pointer
        while fastPointer and fastPointer.next:
		
			#slowPointer moves forward 1 ListNode at a time, fastPointer moves forward 2 ListNodes at a time
            slowPointer, fastPointer = slowPointer.next, fastPointer.next.next
			
            if slowPointer == fastPointer: #if the pointers ever catch up to each other, the LinkedList has a cycle
                return True
        
        return False