class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # og_list= str(x)
        # reverse= og_list[::-1]
        # return og_list==reverse

        if x < 0:
            return False
        n = x    
        rev = 0       
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x //= 10
        
        return rev == n

    
        
        