'''
Problem statement:
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Test cases passed: 208/208
Runtime: 60 ms
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #keep a pointer to each of the two lists
        l1Pointer, l2Pointer = l1, l2
        
        #if neither of the lists is None
        #choose the smaller of the two lists and make a new ListNode from that list's first element
        #then increment appropriate pointer to the next element in list
        if l1 and l2:
            if l1.val > l2.val:
                newList = ListNode(l2.val)
                l2Pointer = l2.next
            else:
                newList = ListNode(l1.val)
                l1Pointer = l1.next
        
        #if either l1 or l2 is None, just make a new list from the other list and just return that
        elif not l1:
            newList = l2
            return newList
        elif not l2:
            newList = l1
            return newList
        
        #pointer to the head of our new list
        newListPointer = newList
        
        #loop thru l1 and l2, splicing new nodes into the new list depending on which is the smaller one
        while l1Pointer and l2Pointer:
            if l1Pointer.val > l2Pointer.val:
                newListPointer.next = l2Pointer
                newListPointer = newListPointer.next
                l2Pointer = l2Pointer.next
            else:
                newListPointer.next = l1Pointer
                newListPointer = newListPointer.next
                l1Pointer = l1Pointer.next
        
        #if l2 was finished first, just make the rest of the list be the rest of l1
        if l1Pointer:
            newListPointer.next = l1Pointer
               
                
        
        #if l1 was finished first, just make the rest of the list be the rest of l2     
        if l2Pointer:
            newListPointer.next = l2Pointer
       
        return newList