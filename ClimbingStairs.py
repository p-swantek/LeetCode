'''
Problem statement:
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Test cases passed: 45/45
Runtime: 44 ms
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: #if there are 2 or less stairs, can only climb that many stairs
            return n
        

		#initialize similarly to the Fibonacci sequence
        first, second, curr = 1, 2, 0
        
		#the amount of steps to reach the top is equal to the amount of steps to reach n-1
		#plus the amount of steps to reach n-2
        for step in range(2, n):
            curr = first + second
            first, second = second, curr
        
        return curr