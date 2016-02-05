'''
Problem statement:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Test cases passed: 600/600
Runtime: 56 ms
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        
        mask = 1 #bit mask
        numOnes = 0 #count of the number of '1' bits
        
        while n > 0: #loop through all the bits in n
			#if bitwise AND between n and mask produces a result of 1, the least significant bit of n was a 1. Increment the count.
            if n & mask == 1: 
                numOnes += 1
            
            n >>= 1 #shift n to check the next bit
            
        return numOnes