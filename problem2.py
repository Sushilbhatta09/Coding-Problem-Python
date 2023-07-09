'''Given an integer x, return true if x is a 
palindrome and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.'''
class Solution(object):
    def isPalindrome(self, x):
        x_t=str(x)
        rev_x=x_t[::-1]
        if x_t==rev_x:
            return True
        else:
            return False
